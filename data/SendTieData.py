"""
@author: wanghongliang
@file: SendTieData.py
@time: 2020/3/22 15:58 
"""
import datetime


class SendTieData(object):
    """用户发帖测试数据"""
    CURRENT_TIME = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    send_pass_data = [
        (
            CURRENT_TIME,
            CURRENT_TIME,
            CURRENT_TIME

        )
    ]
