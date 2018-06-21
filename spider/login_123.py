# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/13'
import requests
import sys
import getpass
from PIL import Image


def run():
    username = input("please input your username: ")
    password = getpass.getpass("please input your password: ")
    session = requests.session()
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
    'Host': 'kyfw.12306.cn'
    }
    login_url = 'https://kyfw.12306.cn/otn/login/init'
    captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'

    # 下一步captcha_url服务器将创建session对象
    code_img = session.get(captcha_url).content
    with open('code.jpg', 'wb') as f:
        f.write(code_img)
    try:
        print('captcha picture will be show, ')
        im = Image.open('code.jpg')
        im.show()
        im.close()
    except ModuleNotFoundError:
        print('图片打开失败')
    code = input('please input captcha:')
    post_data = {
        'answer': code,
        'login_site': 'E',
        'rand': 'sjrand'
    }
    captcha_result = session.post(url, data=post_data, headers=header).json()
    print(captcha_result['result_message'])
    if captcha_result['result_code'] != '4':
        sys.exit()
    form_data = {
        'username': username,
        'password': password,
        'appid': 'otn',
    }
    url = 'https://kyfw.12306.cn/passport/web/login'
    login_result = session.post(url, data=form_data).json()
    print(login_result['result_message'])
    if login_result['result_code'] != 0:
        sys.exit()


if __name__ == '__main__':
    print('12306登陆系统')
    run()

