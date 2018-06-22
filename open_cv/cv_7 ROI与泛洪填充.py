# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
# 填充
import cv2 as cv
import numpy as np

# ROI(region of interest)，经常用来合并图像
# 也就是感兴趣区域，如果你设置了图像了ROI，
# 那么在使用OpenCV的函数的时候，会只对ROI区域操作，其他区域忽略。
# numpy获取ROI
# 泛洪填充，如何填充一个对象内部区域：
# FLOODFILL_FIXED_RANGE：改变图像，泛洪填充
# FLOODFILL_MASK_ONLY：不改变图像，只填充遮罩层本身，忽略新的颜色值参数


def fill_color_demo(img):
    # 定义彩色图像
    copyImg = img.copy()
    h, w = img.shape[:2]
    # 固定 + 2
    mask = np.zeros([h+2, w+2], np.uint8)
    # 起始位置，seedPoint,填充的新值(0,255,255)黄色
    # (100,100,100),(50,50,50)分别是低值高值
    # flag填充方法选择。彩色必须是
    cv.floodFill(
        copyImg, mask, (30, 30),
        (0, 255, 255), (100, 100, 100), (50, 50, 50),
        cv.FLOODFILL_FIXED_RANGE
    )
    cv.imshow('fill_color_demo', copyImg)


def fill_binary_demo():
    image = np.zeros([400, 400, 3], np.uint8)
    # 所有通道255
    image[100:300, 100:300, :] = 255
    cv.imshow('fill_binary_demo', image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('filled binary', image)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
# cv.imshow("input image", src)
# ROI区域：高的50~250，宽度100~300
face = src[0:720, 180:700]
# cv.imshow('face', face)
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# 再次还原成RGB三通道的
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[0:720, 180:700] = backface
# cv.imshow('src', src)
# fill_color_demo(src)
fill_binary_demo()
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
