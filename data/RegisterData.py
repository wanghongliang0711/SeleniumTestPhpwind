# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:15
# @File    : RegisterData.py
import datetime


class RegisterDate(object):
    """用户注册测试数据"""
    CURRENT_TIME = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    register_pass_data = [
        (
            CURRENT_TIME,
            "123456",
            "123456",
            CURRENT_TIME+"@qq.com",
            "恭喜您！亲爱的会员，您已经注册成功。"
        )
    ]

    register_fail_data = [
        (
            "",
            "",
            "",
            "",
            "注册名长度错误,请控制在 3 - 12 字节以内"
        ),
        (
            "12",
            "",
            "",
            "",
            "注册名长度错误,请控制在 3 - 12 字节以内"
        ),
        (
            "12345",
            "",
            "",
            "",
            "密码格式错误：最小值不能少于6"
        )

    ]
