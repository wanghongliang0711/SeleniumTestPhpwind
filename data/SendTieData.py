"""
@author: wanghongliang
@file: SendTieData.py
@time: 2020/3/22 15:58 
"""
import datetime


class SendTieData(object):
    """用户发帖测试数据"""
    CURRENT_TIME = datetime.datetime.now().strftime("%y%m%d%H%M%S")

    send_fail_data = [
        (
            "",
            "",
            "标题不能为空"
        ),
        (
            "title",
            "",
            "文章内容少于 3 个字节"
        ),
        (
            "",
            "text",
            "标题不能为空"
        )
    ]

    send_pass_data = [
        (
            CURRENT_TIME,
            CURRENT_TIME,
            CURRENT_TIME
        ),
        (
            CURRENT_TIME + "_1",
            CURRENT_TIME + "_1",
            CURRENT_TIME + "_1"
        ),
        (
            CURRENT_TIME + "_2",
            CURRENT_TIME + "_2",
            CURRENT_TIME + "_2"
        )
    ]
