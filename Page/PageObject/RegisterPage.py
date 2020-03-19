# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 15:08
# @File    : RegisterPage.py
from Page.BasePage import BasePage
from config.ElementConfig import RegisterElements


class RegisterPage(BasePage):

    def register(self, username, password, confirm_password, email):
        """注册流程"""
        self.open_url()
        self.click_agree()
        self.input_username(username)
        self.input_password(password)
        self.input_cofirm_password(confirm_password)
        self.input_email(email)
        self.click_submit()

    def open_url(self):
        return self.load_url("http://localhost/phpwind732/register.php")

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*RegisterElements.username, username)

    def click_submit(self):
        return self.click(*RegisterElements.submit_register)

    def click_agree(self):
        return self.click(*RegisterElements.agree_btn)

    def clear_username(self):
        return self.clear(*RegisterElements.username)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*RegisterElements.password, password)

    def clear_password(self):
        return self.clear(*RegisterElements.password)

    def input_cofirm_password(self, confirm_password):
        self.clear_confirm_password()
        return self.send_keys(*RegisterElements.confirm_password, confirm_password)

    def clear_confirm_password(self):
        return self.clear(*RegisterElements.confirm_password)

    def input_email(self, email):
        self.clear_email()
        return self.send_keys(*RegisterElements.email, email)

    def clear_email(self):
        return self.clear(*RegisterElements.email)

    def get_error_text(self):
        return self.get_element_text(*RegisterElements.register_error_text)

    def get_pass_text(self):
        return self.get_element_text(*RegisterElements.register_pass_text)
