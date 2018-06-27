# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/06/27'
# 复现计算图中的节点
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import mnist_backward

TEST_INTERVAL_SECS = 5
MNIST_PATH = r'C:\Users\1900\mnist_data'


def test(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
        y = mnist_forward.forward(x, None)

        ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuacy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    print("PATH:"+str(ckpt.model_checkpoint_path))
                    global_step = ckpt.model_checkpoint_path.split('\\')[-1].split('-')[-1]
                    print("global_step",str(global_step))
                    accuacy_score = sess.run(accuacy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
                    print("After %s train steps,test accuracy is %g." % (global_step, accuacy_score))
                else:
                    print("No such model was found!")
                    return
                time.sleep(TEST_INTERVAL_SECS)


def main():
    mnist = input_data.read_data_sets(MNIST_PATH, one_hot=True)
    test(mnist)


if __name__ == '__main__':
    print("Start test")
    main()
