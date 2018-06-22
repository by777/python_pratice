# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
import cv2 as cv
import numpy as np
# 高斯模糊：基于高斯分布


def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaussion_noise(img):
    h, w, c = img.shape
    # 对每一行每一列的每一个像素点三个通道加上一个随机值，
    # 产生随机高斯的随机噪声的图片
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = img[row, col, 0]  # BLUE
            g = img[row, col, 1]  # GREEN
            r = img[row, col, 2]  # RED
            img[row, col, 0] = clamp(b + s[0])
            img[row, col, 1] = clamp(g + s[1])
            img[row, col, 2] = clamp(r + s[2])
    # 发现高斯模糊对高斯噪声有抑制作用
    dst = cv.GaussianBlur(src, (0, 0), 15)
    cv.imshow('gaussion_noise', dst)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
cv.imshow("input image", src)
# dst = cv.GaussianBlur(src, (0, 0), 15)
# cv.imshow('GaussianBlur', dst)
gaussion_noise(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()