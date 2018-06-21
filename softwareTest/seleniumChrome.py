# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/11'

from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait库负责循环等待的
from selenium.webdriver.support.ui import WebDriverWait
# expect_conditions类负责条件
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

'''需要下载Chrome对应版本的chromedriver.exe驱动并添加到path环境变量中'''


def search(shop=None):
    print("开始搜索了")
    driver.get('https://www.taobao.com')
    try:
        input_key = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        input_key.send_keys("{}".format(shop))
        submit = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        submit.click()
        get_response()
    except TimeoutException:
        print("TimeoutException")
        # return search(shop)


def get_response():
    wait.until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))
    )
    # 获取当前网页源代码
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # 用空格简写css selector

    # items = soup.select('.items').
    items = soup.find('div', class_='m-itemlist').find_all('div', class_='item')

    for item in items:
        product = {
            'image': item.find('a').find('img')['src'],
            'price': item.find('div', class_='price g_price g_price-highlight').text,
            'title': item.find('div', class_='row row-2 title').text,
            'purchase_num': item.find('div', class_='deal-cnt').text[:-3],
            'location': item.find('div', class_='location').text

        }
        print(product)


def next_page(page):
    print("当前页数：" + str(page))
    try:
        input_key = wait.until(
            ec.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )[0]

        submit = wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')
        )
        )

        input_key.clear()
        input_key.send_keys(page)
        submit.click()
        wait.until(
            ec.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page))
        )
        # get_response()
    except TimeoutException:
        print("TimeoutException")
        # return next_page(page)


if __name__ == '__main__':
    shop = input("请输入搜素关键字")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    search(shop)
    for i in range(2, 100):
        next_page(i)
