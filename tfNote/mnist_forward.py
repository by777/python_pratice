# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# 描述网络结构
__author__ = 'bai xu'
__date__ = '18/06/18'

import tensorflow as tf
import numpy as np

# 28 * 28
INPUT_NODE = 784
OUTPUT_NODE = 10
# 隐藏层的节点个数
LAYER1_NODE = 500
MNIST_PATH = r'C:\Users\1900\mnist_data'


def get_weight(shape,regularizer):
    w = tf.Variable(tf.truncated_normal(shape,stddev=0.1))
    if regularizer != None:
        tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w


def get_bias(shape):
    b = tf.Variable(tf.zeros(shape))
    return b


def forward(x,regularizer):
    w1 = get_weight([INPUT_NODE,LAYER1_NODE],regularizer)
    b1 = get_bias(LAYER1_NODE)
    y1 = tf.nn.relu(tf.matmul(x,w1)+b1)

    w2 = get_weight([LAYER1_NODE,OUTPUT_NODE], regularizer)
    b2 = get_bias([OUTPUT_NODE])
    y = tf.matmul(y1, w2) + b2
    return y
