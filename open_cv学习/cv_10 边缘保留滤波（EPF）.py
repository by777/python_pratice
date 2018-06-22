# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
'''
边缘（E）保留（P）滤波(F)：
高斯双边 / 均值迁移 / 操作

'''
import cv2 as cv
import numpy as np
# 高斯模糊基于权重的，
# 只考虑了像素空间的分布（正中间的权重大）
# 没有考虑像素值差异的问题
# 像素差异大常常出现在边缘


def bi_demo(img):
    # 高斯双边模糊 - 磨皮
    # 核要小，差异保留下来
    # dst = cv.bilateralFilter(img, 0, 100, 15)
    # 第二个EPF：均值迁移
    # - 类似油画效果
    dst = cv.pyrMeanShiftFiltering(img, 10, 50)
    cv.imshow('bi_demo', dst)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
bi_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
