# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/06/18'

import tensorflow as tf
import numpy as np
''''
八股：
# ####################forward.py
def forward(x,regularizer):
    w =    b =    y =
    return y
def get_weight(shape,regularizer)
def get_bias(shape)
# regular
if regularizer != None:
    tf.add_t_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
-----------------------------
# backward.py
# #############正则化loss
    
 ce =  tf.nn.sparse.softmax_cross_entropy_with_logits(logits=y,label=tf.tf.argmax(y_,1))
 cem = tf.reduce_mean(ce)
 loss = cem + tf.add_n(tf.get_collection('losses'))
 learning_rate = tf.train.exponential_decay(
 LEARNING_RATE_BASE,global_step,LEARNING_RATE_STEP,LEARNING_RATE_DECAY,staircase=True)
 # 滑动平均
 ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,globalz_step)
 ema_op = ema.apply(tf.trainable_variables())
 with tf.control_dependencies([train_step,ema_op]):
    train.op = tf.no_op(name='train’)
################
# ##################### 
def backward(minist):
    x= y_= y = #placeholder
    global_step= loss=
    <正则化、指数衰减学习率、滑动平均>
    train_step=
    实例化saver
    with tf.Session() as sess:
        for i in range(STEPS):
            sess.run(train_step,feed_dict={x: ,y: })
            if i % counter == 0:
                print
                saver.save()
----------------
##########test.py
def test():
    with tf.Graph().as_default() as g:
    # 定义 x y_ y
    实例化可还原滑动平均值的saver
    计算正确率
    while 1:
        with tf.Session() as sess:
            # 加载ckpt模型
            ckpt = tf.train.get_checkpoint_state(PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess,ckpt.model_checkpoint_path)
                    global_step= ckpt.model_checkpoint_path.split('/')[-1]
                    accuracy_score=sess.run(accuracy,feed_dict={x:mnist.test.images,
                    y:mnist.test.labels})
                    print('After %s train steps ,test accuracy = %g' %(global_step,accuracy_score))
                else:
                    print("No check point was found!")
                    return
if __name__ == '__main__':
    mnist = input_data.read_data_sets("./data/",one_hot="True")
    test(mnist)


if __name__ == '__main__':
    pass