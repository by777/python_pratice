# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/22'
# 色彩空间转换API、用inRange通道分离与合并
# 在open cv中，
# H的通道取值是0~180，S是0~255，V是0~255
# 对颜色物体的跟踪非常有用
import cv2 as cv
import numpy as np


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('HSV色彩空间', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('YUV色彩空间', yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('YCrCB色彩空间', ycrcb)


def extract_object_demo():
    # 提取有颜色的对象
    capture = cv.VideoCapture(r"C:\Users\1900\Videos\Captures\capture.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        low_hsv = np.array([0, 0, 0])
        upper_hsv = np.array([180, 255, 46])
        # inRange()得到二值图像
        mask = cv.inRange(hsv, lowerb=low_hsv, upperb=upper_hsv)
        cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            # 27是ESCAPE的意思
            break


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h,w,ch], image.dtype)
    # 调整亮度和对比度，第一个参数contrast对比度
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow('contrast_brightness_demo',dst)

src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
# cv.imshow("input image",src)
# 辟为三个通道
b, g, r = cv.split(src)
# cv.imshow('blue', b)
# 对某一个通道赋值,把红色通道消除
src[:,:,2] = 0
# 通道合并
# src = cv.merge([b,g,r])
# cv.imshow('最后一个通道复制为0',src)
# color_space_demo(src)
# extract_object_demo()
# 对比度1.2 亮度10
contrast_brightness_demo(src,1.2,10)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()