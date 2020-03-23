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
    # login_pass_text = ("xpath", "//a[@id='td_userinfo_more']/span")
    login_pass_text = ("id", "td_userinfo_more")


class RegisterElements(object):
    """注册页面element"""
    agree_btn = ("xpath", "//input[@value='同 意']")
    username = ("id", "regname")
    password = ("id", "regpwd")
    confirm_password = ("id", "regpwdrepeat")
    email = ("id", "regemail")
    submit_register = ("xpath", "//input[@value='提交注册']")
    register_error_text = ("xpath", '//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center')
    register_pass_text = ("xpath", '//*[@id="main"]/div[2]/div[4]/form/table/tbody/tr[1]/td')


class HomePageElements(object):
    """首页element"""
    PHPwind_Board = ("xpath", "//a[contains(@id,'fn_')]")


class ThemePostElements(object):
    """主题帖页面"""
    next_theme = ("link_text", "下一主题")
    theme_name = ("xpath", "//div[@id='breadCrumb']/a[3]")


class BoardPageElements(object):
    """版块element"""
    publish_btn = ("id", "td_post")
    post_tie_zi = ("xpath", "//a[contains(@id,'a_ajax_')]")


class FaTieElements(object):
    """发帖element"""
    title = ("id", "atc_title")
    iframe = ("id", "iframe")
    text = ("xpath", "/html/body")
    sendBtn = ("xpath", "//input[@value='提 交']")
    send_pass_text = ("id", "subject_tpc")
    send_fail_text = ("xpath", '//div[@id="box_container"]/div/div[2]/p')


# "//a[@href="u.php?action=show"]"
# "//*[@id="td_userinfo_more"]/span"

# "//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center/text()"
# "//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center"
