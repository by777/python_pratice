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


def main():
    mnist = input_data.read_data_sets(MNIST_PATH)
    backward(mnist)
    # train_step = tf.train.GradientDescentOptimizer(learning_rate)


if __name__ == '__main__':
    main()