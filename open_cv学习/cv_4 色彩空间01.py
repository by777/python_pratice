# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
色彩空间（Color Space）及相互转换
什么是色彩空间：……
白 255 255 255
绿 + 红 = 黄
常见色彩空间：
RGB、HSV(可以将RGB化繁为简)、HIS、YCrCB（肤色检测用的比较多）、YUV（linux、安卓色彩空间是YUV）
'''
__author__ = 'bai xu'
__date__ = '18/02/22'
import cv2 as cv


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('HSV色彩空间', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('YUV色彩空间', yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('YCrCB色彩空间', ycrcb)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
cv.imshow("input image", src)
color_space_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
