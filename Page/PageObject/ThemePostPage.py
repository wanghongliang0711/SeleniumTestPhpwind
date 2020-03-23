# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 10:59
# @File    : ThemePostPage.py
from Page.BasePage import BasePage
from config.ElementConfig import ThemePostElements


class ThemePostPage(BasePage):

    def click_next_theme_btn(self):
        return self.click(*ThemePostElements.next_theme)

    def get_theme_name(self):
        return self.get_element_text(*ThemePostElements.theme_name)
