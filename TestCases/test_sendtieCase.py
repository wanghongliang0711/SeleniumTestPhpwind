"""
@author: wanghongliang
@file: test_sendtieCase.py
@time: 2020/3/22 16:21 
"""
import pytest
from data.SendTieData import SendTieData


@pytest.mark.skip(reason="暂时跳过")
class TestSendTie(object):
    """测试发帖"""
    success_data = SendTieData.send_pass_data
    fail_data = SendTieData.send_fail_data

    # @pytest.mark.skip(reason="暂时跳过")
    @pytest.mark.parametrize('title, text, expect', fail_data)
    def test_sendtie_fail(self, login, title, text, expect):
        home_page = login[2]
        board_page = login[4]
        sendtie_page = login[3]
        home_page.click_PHPwind_Board_by_random()
        board_page.click_publish()
        sendtie_page.send_tie(title, text)
        actual = sendtie_page.get_fail_text()
        home_page.go_home()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"

    # @pytest.mark.skip(reason="暂时跳过")
    @pytest.mark.parametrize('title, text, expect', success_data)
    def test_sendtie_pass(self, login, title, text, expect):
        home_page = login[2]
        board_page = login[4]
        sendtie_page = login[3]
        home_page.click_PHPwind_Board_by_random()
        board_page.click_publish()
        sendtie_page.send_tie(title, text)
        actual = sendtie_page.get_pass_text()
        home_page.go_home()
        assert actual == expect, f"断言失败 actual:{actual}, expect:{expect}"
