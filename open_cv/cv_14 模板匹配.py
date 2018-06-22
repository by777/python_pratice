# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/03/01'
# 模板匹配： 最简单的、实际环境复杂用处小
# 寻找图片某块带匹配区域
# 必须有模板图像
# 匹配算法
# TM_SQDIFF 平方不同
# TM_SQDIFF_NORMED 越小越相似
# TM_CCORR 相关性
# TM_CCORR_NORMED 相关性因子 越靠近1越相似
# TM_CCOEFF
# TM_CCOEFF_NORMED
import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
    target = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw,tl[1]+th)
        # 绘制矩形
        cv.rectangle(target,tl,br,(0,0,255),12)
        cv.imshow('match-'+np.str(md),target)


src = cv.imread(r"C:\Users\1900\Pictures\demo.jpg")
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
