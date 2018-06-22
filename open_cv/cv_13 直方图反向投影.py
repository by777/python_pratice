# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/27'

# 直方图反向投影 + mean shift：有颜色物体的跟踪
# 如利用地震波反向传播寻找震源、基站定位手机位置
# 多数在HSV色彩空间
import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt


def back_projection():
    sample = cv.imread(r"C:\Users\1900\Desktop\LinuxLogo.jpg")
    target = cv.imread(r"C:\Users\1900\Desktop\WindowsLogo.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    roi_hist = cv.calcHist([roi_hsv],[0, 1],None,[180,256],[0, 180, 0,256])
    # 归一化0~255之间
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
    # 1 不需要放缩
    dst = cv.calcBackProject([target_hsv],[0,1],roi_hist,[0,180,0,256],1)
    cv.imshow("BackProject", dst)


# 计算2d直方图
def hist2d_demo(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # 这次要计算两个通道
    hist = cv.calcHist([img], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow("hist", hist)
    # 差值方式：临近点差值
    plt.imshow(hist, interpolation='nearest')
    plt.title('2D Histgram')
    plt.show()


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# hist2d_demo(src)
back_projection()
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
