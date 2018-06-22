# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/08'
# 分块 就像局部二值化
# 全局阈值 VS 局部阈值
# 图很大二值化噪声也会很大，使用自适应阈值是一个最好的选择，全局阈值会出现各种各样的问题
# 127 ,26其中127必须是奇数，算出来的均值加上20，大于才变成白色，剩下的黑色
# 也可以先resize再二值化，提高代码运行速度
import cv2 as cv
import numpy as np


def big_image_demo(img):
    print(img.shape)
    # 超大的图片 (7749, 5477, 3)
    cw = 256
    ch = 256
    h, w = img.shape[:2]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:col + col]
            # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row + ch, col:col + col] = dst
            # print(np.std(dst), np.mean(dst))
    cv.imwrite("result_binary.png", gray)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
# 创建GUI将图像显示出来
big_image_demo(src)
# 等待下一个用户的响应操作
cv.waitKey(0)
cv.destroyAllWindows()
