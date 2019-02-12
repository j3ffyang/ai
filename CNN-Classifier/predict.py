#!/usr/bin/python
#coding:utf-8

import sys
import tensorflow as tf
import numpy as np
import scipy
from scipy import ndimage


file_path = sys.argv[1]

# with tf.Session() as sess:
sess = tf.Session()
tf.initialize_all_variables().run(session=sess)

graph = tf.get_default_graph()
new_saver = tf.train.import_meta_graph('my_test_model.meta')
new_saver.restore(sess, 'my_test_model')

predict_op = tf.get_collection('predict_op')[0]
dataFlowGraph = tf.get_default_graph()
x = dataFlowGraph.get_tensor_by_name("X:0")

# if __name__ == "__main__":
#     image = np.array(ndimage.imread(file_path, flatten = False))
#     my_image = scipy.misc.imresize(image, size = (224, 224), mode = 'RGB')
#     # my_image = my_image / 255.
#     my_image_work = np.expand_dims(my_image, 0)
#     print("Using a picture of shape", my_image_work.shape, "for the prediction")
#     print (my_image.shape)
#     # img = np.asarray(file_path, dtype='float32') / 256.
#     # image = image.astype('float32')
#     # my_image = image.reshape(1, 64, 64, 3)
#     # tf.reset_default_graph()
#     with tf.Session() as sess:
#         tf.initialize_all_variables().run()
#
#         graph = tf.get_default_graph()
#         new_saver = tf.train.import_meta_graph('my_test_model.meta')
#         # new_saver.restore(sess, 'my_test_model')
#         new_saver.restore(sess, 'my_test_model')
#         predict_op = tf.get_collection('predict_op')[0]
#         dataFlowGraph = tf.get_default_graph()
#         x = dataFlowGraph.get_tensor_by_name("X:0")
#         prediction = sess.run(predict_op, feed_dict = {x: my_image_work})
#         print("\nThe predicted image class is:", str(np.squeeze(prediction)))
#         # predict(my_image_work, parameters, sess)

def predictImage(file_path):
    image = np.array(ndimage.imread(file_path, flatten = False))
    my_image = scipy.misc.imresize(image, size = (224, 224), mode = 'RGB')
    # my_image = my_image / 255.
    my_image_work = np.expand_dims(my_image, 0)
    print("Using a picture of shape", my_image_work.shape, "for the prediction")
    print (my_image.shape)
    prediction = sess.run(predict_op, feed_dict = {x: my_image_work})
    print("\nThe predicted image class is:", str(np.squeeze(prediction)))
    return np.squeeze(prediction)

if __name__ == "__main__":
    image_path = sys.argv[1]
    predict = predictImage(image_path)
