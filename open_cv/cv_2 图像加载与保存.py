# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# 加载与保存
__author__ = 'bai xu'
__date__ = '18/02/21'
import cv2 as cv
import numpy as np

def get_image_info(image):
    print(type(image))
    # 高宽通道数目
    print(image.shape)
    # 像素数据大小
    print(image.size)
    # 字节、每个通道位数占多少
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

def video_demo():
    # 从第一个摄像头读取数据，也可是视频路径
    capture = cv.VideoCapture(0)
    while True:
        # 帧
        ret, frame = capture.read()
        # flip解决左右颠倒(镜像)

        frame = cv.flip(frame, 1)
        cv.imshow('video',frame)
        # 50 ms
        c = cv.waitKey(50)
        if c == 27:
            break
src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
# video_demo()
get_image_info(src)
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite(r'C:\Users\1900\Desktop\result.png',gray)
cv.waitKey(0)
cv.destroyAllWindows()
# 图像属性:
# 通道数目、高与宽、像素数据、位图深度
# Configure Vision
