"""
@author: wanghongliang
@file: test_study_ActionChains_select.py
@time: 2020/3/29 11:44 
"""
import pytest
from data.ActionChainsDate import ActionChainsData


class TestStudyActionChainsSelect(object):
    """学习ActionChains 和 Select"""
    type_view_data = ActionChainsData.type_view_data
    orderway_data = ActionChainsData.orderway_data

    @pytest.mark.skip(reason="暂时跳过")
    @pytest.mark.parametrize('type_text, expect', type_view_data)
    def test_actionchains(self, login, type_text, expect):
        home_page = login[2]
        board_page = login[4]
        home_page.click_PHPwind_Board_by_random()
        board_page.select_type_view(type_text)
        actual = board_page.get_type_view_text()
        home_page.go_home()
        assert expect in actual, f"断言失败 actual:{actual}, expect:{expect}"

    @pytest.mark.parametrize('select, expect', orderway_data)
    def test_select(self, login, select, expect):
        home_page = login[2]
        board_page = login[4]
        home_page.click_PHPwind_Board_by_random()
        board_page.select_orderway(select)
        actual = board_page.get_first_orderway_select_text()
        home_page.go_home()
        assert expect == actual, f"断言失败 actual:{actual}, expect:{expect}"
