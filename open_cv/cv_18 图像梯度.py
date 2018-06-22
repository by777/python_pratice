# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/13'

# 图像梯度：自定义的卷积soble算子
# 一阶导数与Soble算子
# 边缘像素值差异程度 - 导数
# 二阶导数与拉普拉斯算子
# 在二阶导数的时候最大变化处的值为0即边缘是
# 0值。通过二阶导数计算，依据此理论可以计算图像二阶导数，提取边缘
import cv2 as cv
import numpy as np


def sobel_demo(img):
    # x方向梯度
    grad_x = cv.Sobel(img, cv.CV_32F, 1, 0)
    # Sobel的增强边缘，但对噪声敏感
    # grad_x = cv.Scharr(img, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    # cv.imshow("gradient_x",gradx)
    # cv.imshow("gradient_y", gradx)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradxy", gradxy)


def lapalian_demo(img):
    dst = cv.Laplacian(img, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian", lpls)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
