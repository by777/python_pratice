# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/13'
# 提取图像边缘
# Canny算法介绍：
# 是一种很好的边缘检测器，很常用也很实用
# 高斯模糊——GaussianBlur
# 非最大信号抑制
# 高低阈值链接、凡是高于阈值T2的都保留，凡是低于T
# 的都抛弃 T2:T1 = 3:1/2:1
__date__ = '18/02/21'
import cv2 as cv
import numpy as np


def edge_demo(image):
    # 边缘提取
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("canny edge", edge_output)
    # 彩色
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("edge Color", dst)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
edge_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
