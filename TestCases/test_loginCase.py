# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:12
# @File    : test_loginCase.py
from data.LoginData import LoginData
import pytest


@pytest.mark.skip(reason="暂时跳过")
class TestLogin(object):
    login_data = LoginData

    @pytest.mark.parametrize('username, password, expect', login_data.login_pass_data)
    def test_pass(self, open_url, username, password, expect):
        """登录成功测试"""
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_pass_text()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"

    @pytest.mark.skip(reason="暂时跳过")
    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_data)
    def test_fail(self, open_url, username, password, expect):
        """登录失败测试"""
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_error_text()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"


if __name__ == "__main__":
    pytest.main(['-v', 'test_loginCase.py'])
