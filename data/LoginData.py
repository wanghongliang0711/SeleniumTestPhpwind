# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 16:58
# @File    : LoginData.py


class LoginData(object):
    """"用户登录测试数据"""
    login_fail_data = [
        (
            "wang",
            "",
            "用户名或密码为空"
        ),
        (
            "",
            "wang",
            "用户名或密码为空"
        ),
        (
            "wang",
            "wang",
            "用户wang 不存在"
        )

    ]