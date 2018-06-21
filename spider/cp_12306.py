# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'bai xu'
__date__ = '18/02/13'

import requests


def check():
    response = requests.get(
        'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.'
        'train_date=2018-02-13&leftTicketDTO.from_station=CSQ&leftTicketDTO.'
        'to_station=CDW&purpose_codes=ADULT')
    # 长沙 -> 成都 base64
    result = response.json()
    return result['data']['result']


'''软卧 = 23 硬卧 = 28 硬座 = 29 无座 = 26
_json_att:
leftTicketDTO.from_station_name:长沙
leftTicketDTO.to_station_name:成都
leftTicketDTO.from_station:CSQ
leftTicketDTO.to_station:CDW
leftTicketDTO.train_date:2018-02-13
back_train_date:2018-02-13
flag:dc
purpose_code:ADULT
pre_step_flag:index'''

# nu = 0
if __name__ == '__main__':
    for i in check():
        temp_list = i.split('|')
        # for n in temp_list:
        #     print(nu, n)
        #     nu += 1
        # nu = 0
        if temp_list[23] != '无' and temp_list[23] != '':
            print('有票')
