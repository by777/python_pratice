# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/11'
# 尺度空间不变性
# 高斯金字塔、拉普拉斯金字塔
# reduce = 高斯模糊 + 降采样：偶数行（列）取样 逐层递归
# expand = 扩大 + 卷积 升采样
# 从高斯金字塔得到拉普拉斯金字塔
# L1 = g1 - EXPAND(g2)
# PyrDown降采样 PyrUp还原
import cv2 as cv
import numpy as np


def pyramid_demo(img):
    level = 3
    temp = img.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down" + str(i), dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(img):
    # 得到高斯金字塔的结果
    pyramid_images = pyramid_demo(img)
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):
        # 最后一层特殊处理
        if (i - 1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=img.shape[:2])
            lpls = cv.subtract(img, expand)
            cv.imshow("lapalian_down" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow("lapalian_down" + str(i), lpls)


# 图片必须是2的n次方的正方形
src = cv.imread(r"C:\Users\1900\Desktop\workplace\opencv-master\samples\data\lena.jpg")
# pyramid_demo(src)
lapalian_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
