# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 13:09
# @File    : test_next_themeCase.py
import pytest


@pytest.mark.skip(reason="暂时跳过")
class TestNextTheme(object):
    """测试下一主题按钮有效"""

    def test_next_theme(self, login):
        actual = []
        home_page = login[2]
        board_page = login[4]
        theme_page = login[5]
        home_page.click_PHPwind_Board_by_random()
        expect = board_page.all_theme_name()
        board_page.click_first_theme()
        for single_theme in range(len(expect)-1):
            actual.append(theme_page.get_theme_name())
            theme_page.click_next_theme_btn()
        actual.append(theme_page.get_theme_name())
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"
