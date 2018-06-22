# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/23'
import cv2 as cv
import numpy as np
# 直方图均衡化 、 直方图比较
# 如果两张图片相近 那么他们的直方图应该很相似
# 方向直方图 、 角度直方图


# open cv 的直方图均衡化都是基于灰度图
def equal_hist(img):
    # 全局的直方图均衡化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 直方图均衡化能自动调整对比度是图像增强的一个手段
    dst = cv.equalizeHist(gray)
    cv.imshow('equalhist', dst)


def clahe_demo(img):
    # 局部的
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 直方图均衡化能自动调整对比度是图像增强的一个手段
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clahe_demo', dst)


def create_rgb_hist(img):
    h,w,c = img.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = img[row,col,0]
            g = img[row, col, 1]
            r = img[row, col, 2]
            index = np.int((b/bsize)*16*16+(g/bsize)*16*16+(r/bsize)*16*16)
            rgbHist[index, 0] = rgbHist[index, 0] + 1
    return rgbHist

def hist_compare(img1,img2):
    hist1 = create_rgb_hist(img1)
    hist2 = create_rgb_hist(img2)
    # 巴氏距离 - 越小越相似 0 ~ 1
    math1 = cv.compareHist(hist1,hist2, cv.HISTCMP_BHATTACHARYYA)
    # 相关性比较 - 相关性越大越相似 0 ~ 1
    math2 = cv.compareHist(hist1,hist2, cv.HISTCMP_CORREL)
    # 卡方 - 越大越不相似
    math2 = cv.compareHist(hist1,hist2, cv.HISTCMP_CHISQR)

src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# equal_hist(src)
clahe_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
