# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:00
# @File    : conftest.py
from Page.PageObject.LoginPage import LoginPage
from Page.PageObject.RegisterPage import RegisterPage
from Page.PageObject.HomePage import HomePage
from Page.PageObject.FaTiePage import FaTiePage
from Page.PageObject.BoardPage import BoardPage
from Page.PageObject.ThemePostPage import ThemePostPage
from data.LoginData import LoginData
import pytest


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    fatie_page = FaTiePage(driver)
    board_page = BoardPage(driver)
    theme_page = ThemePostPage(driver)
    print("********ini_pages(driver)")
    yield driver, login_page, register_page, home_page, fatie_page, board_page, theme_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    print("********open_url(ini_pages)")
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page, register_page, home_page, fatie_page, board_page, theme_page = ini_pages
    # login_page.open_url()
    login_page.login(LoginData.login_pass_data[0][0], LoginData.login_pass_data[0][1])
    print("********login(ini_pages)")
    yield login_page, register_page, home_page, fatie_page, board_page, theme_page
    driver.delete_all_cookies()
