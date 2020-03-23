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

    def all_theme(self):
        return self.find_Elements(*BoardPageElements.post_tie_zi)

    def click_first_theme(self):
        return self.click(*BoardPageElements.post_tie_zi)

    def all_theme_name(self):
        all_theme = self.all_theme()
        return [name.text for name in all_theme]
