# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/12'

import requests
import getpass
import sys

from PIL import Image
from html.parser import HTMLParser


"""首先拿到一个会话（没有登陆），接下来按照浏览器的格式去发送post请求来登陆
如果登陆成功，session是已经登陆的状态，然后去请求其他的分类"""


class DoubanClient(object):
    def __init__(self):
        # 定义requests的一些参数
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/64.0.3282.140 Safari/537.36',
            'origin': 'https://www.douban.com',
            'Content - Type': 'text / html',
            'charset': 'utf - 8'

        }
        self.ck = None
        self.session = requests.session()
        # 对它的头进行定制
        self.session.headers.update(self.headers)

    def login(self, username, password,
              source='index_nav',
              redir='https://www.douban.com/',
              login='登陆'):
        post_data = {
            'source': source,
            'redir': redir,
            'form_email': username,
            'form_password': password,
            'login': login
        }
        login_url = 'https://accounts.douban.com/login'
        response = self.session.get(login_url)
        (captcha_id, captcha_url) = _get_captcha(response.content)
        # 判断是否出现了验证码
        if captcha_id:
            print('captcha picture will be show, ')
            r = self.session.get(captcha_url)
            with open('captcha.jpg', 'wb') as f:
                f.write(r.content)
            try:
                im = Image.open('captcha.jpg')
                im.show()
                im.close()
            except ModuleNotFoundError:
                print("PIL ModuleNotFound")
            post_data['captcha-id'] = captcha_id
            captcha_solution = input("please input solution of capacha: ")
            post_data['captcha-solution'] = captcha_solution
        self.session.post(login_url, data=post_data, headers=self.headers)
        p = self.session.get('https://www.douban.com/')
        p.encoding = 'utf-8'
        req_headers = p.request.headers
        for key in req_headers:
            if key == 'Cookie':
                # 每个用户都有唯一的ck
                try:
                    self.ck = req_headers[key].split(';')[1].split('=')[1]
                except IndexError:
                    print('登录失败')
                    sys.exit()

    def post_content(self, comment, url="https://www.douban.com/"):
        data = {
            'ck': self.ck,
            'comment': comment
        }
        self.session.post(url, data=data, headers=self.headers)


def _attr(attrs, attrname):
    # attrs是所有的属性，attrname是其中之一
    for attr in attrs:
        # attr由属性名字和值组成
        if attr[0] == attrname:
            return attr[1]
    return None


def _get_captcha(content):
    # 把content交给此类来处理，把里面默认的标签自动解析出来
    # 获取验证码的ID和URL
    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None

        def handle_starttag(self, tag, attrs):
            # 标签、属性
            # attrs是所有属性
            if tag == 'img' and _attr(attrs, 'id') == 'captcha_image' \
                    and _attr(attrs, 'class') == 'captcha_image':
                self.captcha_url = _attr(attrs, 'src')

            if tag == 'input' and _attr(attrs, 'type') == 'hidden' \
                    and _attr(attrs, 'name') == 'captcha-id':
                self.captcha_id = _attr(attrs, 'value')

    p = CaptchaParser()
    # 把需要解析的数据传输给feed方法解析
    # p.feed(content.decode("utf8"))
    p.feed(str(content))
    return p.captcha_id, p.captcha_url


if __name__ == '__main__':
    print("豆瓣自动登陆发帖")
    username = input("please input your username: ")
    password = getpass.getpass("please input your password: ")
    dc = DoubanClient()
    dc.login(username, password)
    comment = input("please input your comment: \n")
    dc.post_content(comment)
