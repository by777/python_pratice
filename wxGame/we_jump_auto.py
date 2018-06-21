# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/01'

from PIL import Image

import time
import random
import os
import json
import re
import subprocess


def get_screen_size():
    screen_size = os.popen('adb shell wm size').read()
    if not screen_size:
        print("请安装adb及环境变量")
        exit()
    m = re.search(r'(\d+)*(\d+)', screen_size)
    if m:
        return "%s*%s" % (m.group(2), m.group(1))


def init():
    screen_size = get_screen_size()
    config_file_path = 'config/%s/config.json' % screen_size
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            print('Load config file from %s' % config_file_path)
            return json.loads(f.read())
    else:
        with open('config/default.json', 'r') as f:
            print('Load config file from config/default.json')
            return json.loads(f.read())


def get_screenshot():
    # 不能输出到标准输出，而是subprocess的管道中
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screen_shot = process.stdout.read()
    screen_shot = screen_shot.replace(b'\r\r\n', b'\n')
    with open('auto.png', 'wb') as f:
        f.write(screen_shot)


def find_piece_board(img, config):
    # 获取图片的宽和高
    w, h = img.size
    print("w: " + str(w) + "h: " + str(h))
    # 扫描起始y坐标
    scan_start_y = 0
    # 棋子的最大y坐标
    piece_y_max = 0
    # 从上往下扫描棋子，还要尽量减少开销
    # 图片的像素矩阵
    img_pixel = img.load()
    # 以50像素为步长测试出最高点
    for i in range(h//3, h*2//3, 50):
        # 每拿到一行的第一个像素点
        # 每一个像素里面有4个值，前三个代表RGB
        first_pixel = img_pixel[0, i]
        for j in range(1, w):
            img_pixel = img_pixel[j, i]
            # 如果不是纯色的--跳出，说明找到了y轴的最大值
            if first_pixel[:-1] != img_pixel[:-1]:
                scan_start_y = i - 50
                break
        if scan_start_y:
            break
    # 开始扫描棋子
    left = 0
    right = 0
    for i in range(scan_start_y, h*2//3):
        flag = True
        for j in range(w//8, w*7//8):#切掉左右1/8
            pixel = img_pixel[j, i]
            # 根据棋子的颜色判断，找到最后一行的点的起始后末尾
            if (50 < pixel[0] < 60) and \
                    (53 < pixel[1] < 63) and \
                    (95 < pixel[2] < 110):
                # 用ps分析看的来的
                if flag:# 为真说明每一行第一次碰到棋子
                    left = j# 最后一行的最左和最右
                    flag = False
                    right = j
                    piece_y_max = max(i, piece_y_max)# 最大Y坐标
    piece_x = (left + right) // 2
    piece_y = piece_y_max - config['piece_base_height_1_2']



def jump(distance, press_ratio):
    '''跳一段距离'''


def run():
    # 获取配置，检查环境
    config = init()
    print(config)
    while True:
        get_screenshot()
        # 分析棋子棋盘坐标
        img = Image.open('auto.png')
        # 棋子横纵坐标、棋盘横纵坐标
        piece_x, piece_y, board_x, board_y = find_piece_board(img, config)
        # distance = ((piece_x - board_x) ** 2 + (piece_y - board_y) ** 2)**0.5
        # jump(distance, config['press_coefficient'])
        # 随机间隔时间1~3，random.random()获取0~1之间的随机数
        time.sleep(1 + random.random() * 2)


if __name__ == '__main__': 
    run() 
