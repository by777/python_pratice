# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
# 模糊操作 - 离散卷积的小块叠加
# 均值模糊、中值模糊、自定义模糊
# 基本原理：
# / 基于离散卷积 / 定义好每个卷积核 / 不同卷积核得到不同的结果 / 模糊是卷积的一种表象
# 卷积大小可以改变内容open cv固定

import cv2 as cv
import numpy as np


# 均值模糊:可以去除噪声（对随机噪声）
def blur_demo(img):
    # (1,3) ksize 卷积核 1行三列
    dst = cv.blur(img, (15, 1))
    cv.imshow('blur', dst)


# 中值模糊可以去除椒盐噪声
def median_blur_demo(img):
    dst = cv.medianBlur(img, 5)
    cv.imshow('median_blur_demo', dst)


# 更加灵活的方式模糊处理
def custom_blur_demo(img):
    kernel = np.ones([5, 5], np.float32) / 25
    # 锐化
    # kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    dst = cv.filter2D(img, -1, kernel=kernel)
    cv.imshow('custom_blur_demo', dst)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
cv.imshow("input image", src)
# blur_demo(src)
# median_blur_demo(src)
custom_blur_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
