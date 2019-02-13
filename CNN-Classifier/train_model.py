#!/usr/bin/python
#coding:utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
import tensorflow as tf
from tensorflow.python.framework import ops
from tools.cnn_utils import *
from tools.dataset import *
import os
from vggnet_16 import *
import vgg16
import time
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def get_datasets(train_set, test_set):
    """
    Get transet and test set, and convert them to valid metrixs.
    Arguments:
    train_set -- train set file path
    test_set -- test set file path
    """
    X_train_orig, Y_train_orig, X_test_orig, Y_test_orig = load_dataset(train_set, test_set)

    X_train = X_train_orig/255.
    X_test = X_test_orig/255.
    Y_train = convert_to_one_hot(Y_train_orig, 2).T
    Y_test = convert_to_one_hot(Y_test_orig, 2).T
    # Y_train = Y_train_orig.reshape(96, 1)
    # Y_test = Y_test_orig.reshape(25, 1)

    return X_train, Y_train, X_test, Y_test

def create_placeholders(n_H0, n_W0, n_C0, n_y):

    X = tf.placeholder(tf.float32, [None, n_H0, n_W0, n_C0], name = "X")
    Y = tf.placeholder(tf.float32, [None, n_y], name = "Y")

    return X, Y

def initialize_parameters():

    # You don't need to declare Bias1 and Bias2 since tf.get_variable has already considerd bias.
    W1 = tf.get_variable("W1", [4,4,3,8], initializer = tf.contrib.layers.xavier_initializer(seed = 0))
    W2 = tf.get_variable("W2", [2,2,8,16], initializer = tf.contrib.layers.xavier_initializer(seed = 0))

    parameters = {"W1": W1,
                  "W2": W2}

    return parameters

# GRADED FUNCTION: forward_propagation

def forward_propagation(X, parameters):

    # Retrieve the parameters from the dictionary "parameters"
    W1 = parameters['W1']
    W2 = parameters['W2']

    # CONV2D: stride of 1, padding 'SAME'
    Z1 = tf.nn.conv2d(X, W1, strides = [1, 1, 1, 1], padding = 'SAME')
    # RELU
    A1 = tf.nn.relu(Z1)
    # MAXPOOL: window 8x8, sride 8, padding 'SAME'
    P1 = tf.nn.max_pool(A1, ksize = [1, 8, 8, 1], strides = [1,8, 8, 1], padding = 'SAME')
    # CONV2D: filters W2, stride 1, padding 'SAME'
    Z2 = tf.nn.conv2d(P1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
    # RELU
    A2 = tf.nn.relu(Z2)
    # MAXPOOL: window 4x4, stride 4, padding 'SAME'
    P2 = tf.nn.max_pool(A2, ksize = [1, 4, 4, 1], strides = [1, 4, 4, 1], padding = 'SAME')
    # FLATTEN
    P2 = tf.contrib.layers.flatten(P2)

    # FULLY-CONNECTED without non-linear activation function (not not call softmax).
    # 6 neurons in output layer. Hint: one of the arguments should be "activation_fn=None"
    Z3 = tf.contrib.layers.fully_connected(P2, 3, activation_fn=None)

    return Z3

# GRADED FUNCTION: compute_cost

def compute_cost(Z3, Y):

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = Z3, labels = Y))

    return cost

# GRADED FUNCTION: model

def model(train_set_path, test_set_path, learning_rate = 1e-4,
          num_epochs = 3, minibatch_size = 1, print_cost = True):
    X_train, Y_train, X_test, Y_test = get_datasets(train_set_path, test_set_path)
    ops.reset_default_graph()                         # to be able to rerun the model without overwriting tf variables
    tf.set_random_seed(1)                             # to keep results consistent (tensorflow seed)
    seed = 3                                          # to keep results consistent (numpy seed)
    (m, n_H0, n_W0, n_C0) = X_train.shape
    n_y = Y_train.shape[1]
    costs = []                                        # To keep track of the cost

    X, Y = create_placeholders(n_H0, n_W0, n_C0, n_y)

    parameters = initialize_parameters()

    Z3 = forward_propagation(X, parameters)

    cost = compute_cost(Z3, Y)
    ### END CODE HERE ###

    optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(cost)

    init = tf.global_variables_initializer()



    # Start the session to compute the tensorflow graph
    with tf.Session() as sess:

        # Run the initialization
        sess.run(init)
        # _ , c = sess.run([optimizer, cost], feed_dict={X: X_train, Y: Y_train})

        # costs.append(c)
        # Do the training loop
        for epoch in range(num_epochs):

            minibatch_cost = 0.
            num_minibatches = int(m / minibatch_size) # number of minibatches of size minibatch_size in the train set
            seed = seed + 1
            minibatches = random_mini_batches(X_train, Y_train, minibatch_size, seed)

            for minibatch in minibatches:

                # Select a minibatch
                (minibatch_X, minibatch_Y) = minibatch
                # IMPORTANT: The line that runs the graph on a minibatch.
                # Run the session to execute the optimizer and the cost, the feedict should contain a minibatch for (X,Y).
                ### START CODE HERE ### (1 line)
                _ , temp_cost = sess.run([optimizer, cost], feed_dict={X: minibatch_X, Y: minibatch_Y})
                ### END CODE HERE ###

                minibatch_cost += temp_cost / num_minibatches


            # Print the cost every epoch
            if print_cost == True and epoch % 1 == 0:
                print ("Cost after epoch %i: %f" % (epoch, minibatch_cost))
            if print_cost == True and epoch % 1 == 0:
                costs.append(minibatch_cost)


        predict_op = tf.argmax(Z3, 1)
        correct_prediction = tf.equal(predict_op, tf.argmax(Y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(accuracy)
        train_accuracy = accuracy.eval({X: X_train, Y: Y_train})
        test_accuracy = accuracy.eval({X: X_test, Y: Y_test})
        print(train_accuracy, test_accuracy)
        print(Y_train)
        # save trained model
        saver = tf.train.Saver()
        tf.add_to_collection('predict_op', predict_op)
        saver.save(sess, './my_test_model')

        return train_accuracy, test_accuracy, parameters

def modelVGGNet16(train_set_path, test_set_path, learning_rate = 2e-3,
          num_epochs = 15, minibatch_size = 1, print_cost = True):
    X_train, Y_train, X_test, Y_test = get_datasets(train_set_path, test_set_path)
    ops.reset_default_graph()                         # to be able to rerun the model without overwriting tf variables
    tf.set_random_seed(1)                             # to keep results consistent (tensorflow seed)
    seed = 3                                          # to keep results consistent (numpy seed)
    (m, n_H0, n_W0, n_C0) = X_train.shape
    n_y = Y_train.shape[1]
    costs = []                                        # To keep track of the cost

    X, Y = create_placeholders(n_H0, n_W0, n_C0, n_y)

    parameters = initialize_parameters()

    Z3 = inference_op(X, 1)

    cost = compute_cost(Z3, Y)
    ### END CODE HERE ###

    optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

    init = tf.global_variables_initializer()



    # Start the session to compute the tensorflow graph
    with tf.Session() as sess:

        # Run the initialization
        sess.run(init)
        # _ , c = sess.run([optimizer, cost], feed_dict={X: X_train, Y: Y_train})

        # costs.append(c)
        # Do the training loop
        for epoch in range(num_epochs):

            minibatch_cost = 0.
            num_minibatches = int(m / minibatch_size) # number of minibatches of size minibatch_size in the train set
            seed = seed + 1
            minibatches = random_mini_batches(X_train, Y_train, minibatch_size, seed)
            print(epoch)
            for minibatch in minibatches:

                # Select a minibatch
                (minibatch_X, minibatch_Y) = minibatch
                # IMPORTANT: The line that runs the graph on a minibatch.
                # Run the session to execute the optimizer and the cost, the feedict should contain a minibatch for (X,Y).
                ### START CODE HERE ### (1 line)
                _ , temp_cost = sess.run([optimizer, cost], feed_dict={X: minibatch_X, Y: minibatch_Y})
                ### END CODE HERE ###

                minibatch_cost += temp_cost / num_minibatches


            # Print the cost every epoch
            print ("Cost after epoch %i: %f" % (epoch, minibatch_cost))

            # if print_cost == True and epoch % 5 == 0:
            #     print ("Cost after epoch %i: %f" % (epoch, minibatch_cost))
            if print_cost == True and epoch % 1 == 0:
                costs.append(minibatch_cost)


        predict_op = tf.argmax(Z3, 1)
        correct_prediction = tf.equal(predict_op, tf.argmax(Y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(accuracy)
        train_accuracy = accuracy.eval({X: X_train, Y: Y_train})
        test_accuracy = accuracy.eval({X: X_test, Y: Y_test})
        # print train_accuracy, test_accuracy
        # save trained model
        saver = tf.train.Saver()
        tf.add_to_collection('predict_op', predict_op)
        saver.save(sess, './my_test_model')

        return train_accuracy, test_accuracy, parameters

def pretrained_vgg16_model(image_path, starter_learning_rate = 0.07,
          num_epochs = 10, minibatch_size = 1, print_cost = True):
    # load all image address into memory
    train_addrs, train_labels, test_addrs, test_labels = list_images_and_lables(image_path)
    # process train lables and test labels to np.array format
    train_labels = np.array(train_labels)
    # shape[0] = qty of img
    train_labels = train_labels.reshape((1, train_labels.shape[0]))
    # maintain dimensions. 2= 2 classifications = indoor + outdoor.
    # T= matrix reshape
    Y_train = convert_to_one_hot(train_labels, 2).T
    test_labels = np.array(test_labels)
    test_labels = test_labels.reshape((1, test_labels.shape[0]))
    Y_test = convert_to_one_hot(test_labels, 2).T
    # X_train, Y_train, X_test, Y_test = get_datasets(train_set_path, test_set_path)
    ops.reset_default_graph()                         # to be able to rerun the model without overwriting tf variables
    # Fix me!! this code could just train VGG because the diamention is (224, 224, 3)
    (m, n_H0, n_W0, n_C0) = (len(train_addrs), 224, 224, 3) # length* width, 3= rgb
    n_y = Y_train.shape[1]  # len of y_train
    costs = []                                        # To keep track of the cost

    X, Y = create_placeholders(n_H0, n_W0, n_C0, n_y)

    # load pretrained vgg16 model
    vgg = vgg16.Vgg16()
    with tf.name_scope("content_vgg"):
        # load VGG16
        vgg.build(X)

    # add own fully_connected layer # add customized weight. vgg.prob= output
    fc = tf.contrib.layers.fully_connected(vgg.prob, 1024)
    # with tf.name_scope("final_fc"):
    logits = tf.contrib.layers.fully_connected(fc, 2, activation_fn=None)   # 2= classification. possible output of 2= [0.1, 0.9], eg. 0.9 will be chosen

    cost = compute_cost(logits, Y)
    ### END CODE HERE ###

    # tvars = tf.trainable_variables()

    learning_rate = tf.train.exponential_decay(starter_learning_rate, 200,
                                               10, 0.96, staircase=False)
    optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)    # tf template optimization

    init = tf.global_variables_initializer()


    # Start the session to compute the tensorflow graph
    with tf.Session() as sess:

        # Run the initialization
        sess.run(init)
        # _ , c = sess.run([optimizer, cost], feed_dict={X: X_train, Y: Y_train})

        # costs.append(c)
        # Do the training loop
        for epoch in range(num_epochs):
            start_time = time.time()
            minibatch_cost = 0.
            num_minibatches = int(m / minibatch_size) # number of minibatches of size minibatch_size in the train set
            minibatches = random_minibatches(train_addrs, Y_train, minibatch_size)

            for minibatch in minibatches:

                # Select a minibatch
                (minibatch_X, minibatch_Y) = minibatch
                images = []
                for addr in minibatch_X:
                    img = cv2.imread(addr)
                    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    images.append(img)

                minibatch_X = np.array(images)/255.
                # IMPORTANT: The line that runs the graph on a minibatch.
                # Run the session to execute the optimizer and the cost, the feedict should contain a minibatch for (X,Y).
                ### START CODE HERE ### (1 line)
                _ , temp_cost = sess.run([optimizer, cost], feed_dict={X: minibatch_X, Y: minibatch_Y})
                ### END CODE HERE ###

                minibatch_cost += temp_cost / num_minibatches


            # Print the cost every epoch
            if print_cost == True and epoch % 1 == 0:
                print(("build model finished: %ds" % (time.time() - start_time)))
                print ("Cost after epoch %i: %f" % (epoch, minibatch_cost))
            if print_cost == True and epoch % 1 == 0:
                costs.append(minibatch_cost)


        predict_op = tf.argmax(logits, 1)
        correct_prediction = tf.equal(predict_op, tf.argmax(Y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        # Just use a part of training data here.
        train_images = []
        for addr in train_addrs[0:80]:
            img = cv2.imread(addr)
            img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            train_images.append(img)

        X_train = np.array(train_images)/255.
        train_accuracy = accuracy.eval({X: X_train, Y: Y_train[0:80, :]})
        # train_accuracy = accuracy.eval({X: X_train, Y: Y_train})
        test_images = []
        for addr in test_addrs:
            img = cv2.imread(addr)
            img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            test_images.append(img)
        X_test = np.array(test_images)/255.
        test_accuracy = accuracy.eval({X: X_test, Y: Y_test})
        print(train_accuracy, test_accuracy)
        # save trained model
        saver = tf.train.Saver()
        tf.add_to_collection('predict_op', predict_op)
        saver.save(sess, './my_test_model')

        return

if __name__ == "__main__":
    # image_path = sys.argv[1]
    pretrained_vgg16_model('/home/jeff/instguid.git/ai/CNN-Classifier/create-dataset/images/*.jpg')
