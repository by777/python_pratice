# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# 像素运算：算数运算、逻辑运算
# 要求图像大小、dtype相同
# 算术运算：加减乘除 -> 调节亮度、对比度
# 逻辑运算：与或非 -> 遮罩层控制
# 常见图像混算法运算与几何运算
__author__ = 'bai xu'
__date__ = '18/02/22'
import cv2 as cv
import numpy as np


def add_demo(img1, img2):
    dst = cv.add(img1, img2)
    cv.imshow('add demo', dst)


def subtract_demo(img1, img2):
    dst = cv.subtract(img1, img2)
    cv.imshow('subtract', dst)


def divide_demo(img1, img2):
    dst = cv.divide(img1, img2)
    cv.imshow('divide', dst)


def multiply_demo(img1, img2):
    dst = cv.multiply(img1, img2)
    cv.imshow('multiply', dst)


def others(img1, img2):
    m1 = cv.mean(img1)
    m2 = cv.mean(img2)
    h, w = img1.shape[:2]
    # 方差
    M1, dev1 = cv.meanStdDev(img1)
    # 方差即对比度
    print('M1 M2', m1, m2)
    print('M1 dev1', M1, dev1)
    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print('m, dev', m, dev)


def logic_demo(img1, img2):
    # and（与）运算 0 与非0  -> 0

    dst = cv.bitwise_and(img1, img2)
    dst = cv.bitwise_or(img1, img2)# 所有非0的都会有输出
    dst = cv.bitwise_not(img1) # 按位取反
    cv.imshow('logic_demo', dst)


# LinuxLogo.jpg只有黑白，称为mask，可以作为遮罩层
src1 = cv.imread(r"C:\Users\1900\Desktop\LinuxLogo.jpg")
src2 = cv.imread(r"C:\Users\1900\Desktop\WindowsLogo.jpg")
# print(src1.shape,src2.shape)
# 创建GUI将图像显示出来
# cv.namedWindow("image1",cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
# cv.imshow("image1",src1)
# cv.imshow("image2",src2)
# 等待下一个用户的响应操作
# add_demo(src2,src1)
# subtract_demo(src1, src2)
# divide_demo(src1,src2)
# multiply_demo(src1, src2)
# others(src1, src2)
logic_demo(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()