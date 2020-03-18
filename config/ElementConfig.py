# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 15:31
# @File    : ElementConfig.py


class LoginPageElements(object):
    """登录页面element"""
    username = ("xpath", '//input[@name="pwuser"]')
    password = ("xpath", '//input[@name="pwpwd"]')
    loginBtn = ("xpath", '//input[@name="submit"]')
    register = ("link_text", '马上注册')
    login_error_text = ("xpath", '//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center')
    return_continue = ("xpath", '//input[@value="返 回 继 续 操 作"]')

# "//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center/text()"
# "//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center"