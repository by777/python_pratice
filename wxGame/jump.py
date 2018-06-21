# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/01/31'

import os
import math
import time
import PIL
import numpy as np
import matplotlib.pyplot as plt

# 刷新图片用
from matplotlib.animation import FuncAnimation
# 更新锁
need_update = True


def get_screen_image():
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")
    # PIL是专门用于图像操作的包，直接打开它不能用在matplotlib中，需要用到numpy
    image = PIL.Image.open("screen.png")
    # np将图片转换为多维数组
    image_array = np.array(image)
    return image_array


def jump_to_next(point1, point2):
    # 计算弦长
    x1, y1 = point1
    x2, y2 = point2
    # distance是两点之间的斜边
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)
    # 四个坐标分别为按下去的横坐标、按下去的纵坐标、抬起来的横坐标、抬起来的纵坐标、按压时长
    os.system("adb shell input swipe 320 410 320 410 {}".format(int(distance * 1.35)))


def on_click(event, coor=[]):
    # 专门用来做回调的函数，单击做的图之后的回调：
    # event是自动传进去的，是点击事件的坐标位置
    # coor：[(x,y),(x2,y2)]
    global need_update
    coor.append((event.xdata, event.ydata))
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (event.button, event.x, event.y, event.xdata, event.ydata))
    if len(coor) == 2:
        # 退栈，传入两个坐标
        jump_to_next(coor.pop(), coor.pop())
    need_update = True


def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        # 重画图片
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,


if __name__ == '__main__':
    # 实例化一个空白的图片对象
    figure = plt.figure()
    # 将拿到的图片画在坐标轴上，imshow——开始画
    axes_image = plt.imshow(get_screen_image(), animated=True)
    # 先找起始点和落地点：使用鼠标点击事件，绑定事件on_click# 注意不要括号
    figure.canvas.mpl_connect('button_press_event', on_click)
    # 参数一：刷新的对象；参数二：更新的图片；参数三：刷新时间（ms）
    ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
    plt.show()