# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/21'
import cv2 as cv
import numpy as np


# 读取像素遍历访问
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv

    cv.imshow("pixels_demo", image)


def create_image():
    '''多通道'''
    # img = np.zeros([400,400,3],np.uint8)
    # 修改第一个通道的值
    # 绿色
    # img[:,:,1] = np.ones([400,400]) * 255
    # 红色
    # img[:, :, 2] = np.ones([400, 400]) * 255
    """单通道"""
    # img = np.zeros([400,400,1],np.uint8)

    # img[: , :, 0] = np.ones([400,400]) * 127
    # 单通道的灰度
    # 等价于：
    # img.ones([400,400,1],uint8)
    # img = img * 127
    # cv.imshow('new image',img)
    # 初始化一个二维的
    m1 = np.ones([3, 3], dtype=np.uint8)

    m1.fill(122.388)
    print(m1.reshape([1, 9]))


def inverse(img):
    # 像素取反
    dst = cv.bitwise_not(img)
    cv.imshow('inverse', dst)


src = cv.imread(r'C:\Users\1900\Pictures\demo.jpg')
# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input image', src)
t1 = cv.getTickCount()
# create_image()
inverse(src)
# access_pixels(src)
t2 = cv.getCPUTickCount()
print('time (ms):', 1000 * (t2-t1)/cv.getTickFrequency())
cv.waitKey(0)
cv.destroyAllWindows()