# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

'''
图像直方图（histogram）：
一维与多维
操作
matplotlib
'''


def plot_demo(img):
    # 统计的是RGB三通道所有的像素当中是0~255的数目
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def imgage_hist(img):
    # 图像的直方图
    # 图像的三通道
    color = ("Blue", "Green", "Red")
    for i, color in enumerate(color):
        hist = cv.calcHist(
            [img], [i], None, [256],
        [0, 256]
        )
        plt.plot(hist,color=color)
        plt.xlim([0, 256])
        plt.show()


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 等待下一个用户的响应操作
# plot_demo(src)
imgage_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()
