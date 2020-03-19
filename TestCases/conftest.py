# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:00
# @File    : conftest.py
from Page.PageObject.LoginPage import LoginPage
from Page.PageObject.RegisterPage import RegisterPage
import pytest


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    register_page = RegisterPage(driver)
    print("********ini_pages(driver)")
    yield driver, login_page, register_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    print("********open_url(ini_pages)")
    yield login_page
    driver.delete_all_cookies()





