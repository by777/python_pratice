# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/06'

# 二值图像（Binary Image）
# 0 - 黑色； 1 代表255（黑色）
# 图像二值化方法
# 全局阈值 和 局部阈值
# open cv 中二值化方法：
# - OTSU（内方差最小，外方差最大）
# - Triangle
# - 自动与手动
# 自适应阈值（局部阈值）cv.THRESH_OTSU
import cv2 as cv
import numpy as np


def threshold_demo(img):
    # 全局阈值
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    # 也可以是手动指定，最常用
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY )
    # 其他
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY | cv.THRESH_TRUNC)
    print('threshold value',ret)
    cv.imshow("binary", binary)


def local_threshold_demo(img):
    # 全局阈值
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.ADAPTIVE_THRESH_GAUSSIAN_C 求均值时带上高斯权重，最中心的权重越大，更适合做二值化
    # blocksize 必须是奇数，c是常量， 均值减去这个大于10的话才设为白色或者黑色，可以去除噪声影响
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("local_threshold_demo", dst)


def custom_threshold_demo(img):
    # 自计算的均值进行二值化的分割
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    cv.imshow("local_threshold_demo", dst)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# threshold_demo(src)
local_threshold_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

