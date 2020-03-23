"""
@author: wanghongliang
@file: FaTiePage.py
@time: 2020/3/22 15:30 
"""
from Page.BasePage import BasePage
from config.ElementConfig import FaTieElements
# import time


class FaTiePage(BasePage):
    """发帖页"""

    def send_tie(self, title, text):
        self.input_title(title)
        self.switch_frame()
        self.input_main_text(text)
        self.switch_default_frame()
        self.click_send_btn()

    def clear_title(self):
        return self.clear(*FaTieElements.title)

    def input_title(self, title):
        self.clear_title()
        return self.send_keys(*FaTieElements.title, title)

    def switch_frame(self):
        return self.switch_to_frame(*FaTieElements.iframe)

    def switch_default_frame(self):
        return self.switch_to_default_frame()

    def input_main_text(self, text):
        return self.send_keys(*FaTieElements.text, text)

    def click_send_btn(self):
        return self.click(*FaTieElements.sendBtn)

    def get_pass_text(self):
        return self.get_element_text(*FaTieElements.send_pass_text)

    def get_fail_text(self):
        return self.get_element_text(*FaTieElements.send_fail_text)
