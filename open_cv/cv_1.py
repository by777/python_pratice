# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/21'
import cv2 as cv
import numpy as np
src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# 显示图片在创建的窗口上面，通过名字来寻找
cv.imshow("input image", src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()

