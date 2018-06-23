# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/06/20'

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import os

REGULARIZER = 0.0001
LEARNING_RATE_BASE = 0.1
BATCH_SIZE = 200
LEARNING_RATE_DECAY = 0.99
STEPS = 50000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = './model'
MODEL_NAME = 'mnist_model'
MNIST_PATH = r'C:\Users\1900\mnist_data'


def backward(mnist):
    x = tf.placeholder(tf.float32,[None,mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32,[None,mnist_forward.INPUT_NODE])
    y = mnist_forward.forward(x,REGULARIZER)
    gloal_step = tf.Variable(0,trainable=False)

    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(x,REGULARIZER)
    cem = tf.reduce_mean(ce)
    # 调用包含正则化的损失函数
    loss = cem + tf.add_n(tf.get_collection('losses'))

    learnin_rate - tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        gloal_step,
        mnist.train.num.examples / BATCH_SIZE,
        LEARNING_RATE_DECAY,
        staircase=True
    )
    train_step = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss,gloal_step=gloal_step)
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,gloal_step)
    ema_op = ema.apply(tf.trainable_variables())

    with tf.control_dependencies([train_step,emp_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

    for i in range(STEPS):
        xs, ys = mnist.train.next_batch(BATCH_SIZE)
        _, loss_value, step = sess.run([train_op,loss,gloal_step], feed_dict={x:xs,y_:ys})
        if i % 1000 == 0:
            print("After %d train steps, loss on training batch is %g." % (step,loss_value))
            saver.save(sess,os.join(MODEL_SAVE_PATH,MODEL_NAME),global_step=p=gloal_step)

def main():
    mnist = input_data.read_data_sets(MNIST_PATH,one_hot=True)
    backward()



if __name__ == '__main__':
    main()