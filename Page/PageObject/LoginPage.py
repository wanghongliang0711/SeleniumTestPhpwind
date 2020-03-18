# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 15:29
# @File    : LoginPage.py
from Page.BasePage import BasePage
from config.ElementConfig import LoginPageElements


class LoginPage(BasePage):


    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        return self.load_url("http://localhost/phpwind732/login.php")

    def click_login_btn(self):
        return self.click(*LoginPageElements.loginBtn)

    def clear_username(self):
        return self.clear(*LoginPageElements.username)

    def clear_password(self):
        return self.clear(*LoginPageElements.password)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPageElements.username, username)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPageElements.password, password)

    def get_error_text(self):
        return self.get_element_text(*LoginPageElements.login_error_text)

    def click_return_continue_login(self):
        return self.click(*LoginPageElements.return_continue)
