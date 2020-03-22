"""
@author: wanghongliang
@file: BoardPage.py
@time: 2020/3/22 15:22 
"""
from Page.BasePage import BasePage
from config.ElementConfig import BoardPageElements


class BoardPage(BasePage):
    """版块页面"""

    def click_publish(self):
        return self.click(*BoardPageElements.publish_btn)
