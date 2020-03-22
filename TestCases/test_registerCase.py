# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:22
# @File    : test_registerCase.py
from data.RegisterData import RegisterDate
import pytest


@pytest.mark.skip(reason="暂时跳过")
class TestRegister(object):
    register_data = RegisterDate

    @pytest.mark.parametrize('username, password, confirm_password, email, expect', register_data.register_fail_data)
    def test_fail(self, ini_pages, username, password, confirm_password, email, expect):
        """注册失败测试"""
        register_page = ini_pages[2]
        register_page.register(username, password, confirm_password, email)
        actual = register_page.get_error_text()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"

    @pytest.mark.parametrize('username, password, confirm_password, email, expect', register_data.register_pass_data)
    def test_pass(self, ini_pages, username, password, confirm_password, email, expect):
        """注册成功测试"""
        register_page = ini_pages[2]
        register_page.register(username, password, confirm_password, email)
        actual = register_page.get_pass_text()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"
