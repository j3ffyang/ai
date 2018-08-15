import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

inputs = tf.placeholder('float', [None, 2], name='Input')
targets = tf.placeholder('float', name='Target')

weight1=tf.Variable(tf.random_normal(shape=[2,3],stddev=0.02),name="Weight1")
biases1=tf.Variable(tf.random_normal(shape=[3],stddev=0.02),name="Biases1")
tf.summary.histogram("weight_1",weight1)

hLayer=tf.matmul(inputs,weight1)
hLayer=hLayer+biases1
hLayer=tf.sigmoid(hLayer, name='hActivation')

weight2=tf.Variable(tf.random_normal(shape=[3,1],stddev=0.02),name="Weight2")
biases2=tf.Variable(tf.random_normal(shape=[1],stddev=0.02),name="Biases2")
tf.summary.histogram("weight_2",weight2)

output=tf.matmul(hLayer,weight2)
output=output+biases2
output=tf.sigmoid(output, name='outActivation')

cost=tf.squared_difference(targets ,output)
cost=tf.reduce_mean(cost)
tf.summary.scalar("cost", cost)

optimizer=tf.train.AdamOptimizer().minimize(cost)

#generating inputs
import numpy as np

inp=[[0,0],[0,1],[1,0],[1,1]]
out=[[0],[1],[1],[0]]

inp=np.array(inp)
out=np.array(out)

epochs=10 # number of time we want to repeat
import datetime
with tf.Session() as sess:
    summaryMerged = tf.summary.merge_all()
    filename="./summary_log/run"+datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%s")
    writer = tf.summary.FileWriter(filename, sess.graph)
    tf.global_variables_initializer().run()
    for i in range(epochs):
        error,_,sumOut =sess.run([cost,optimizer,summaryMerged],feed_dict={inputs: inp,targets:out})
        # print(i,error) # we dont need this anymore
        writer.add_summary(sumOut,i)

