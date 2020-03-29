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

    def move_to_element_type_view(self):
        return self.move_to_element(*BoardPageElements.move_to_type_view)

    def move_to_type_view(self, type_text):
        self.move_to_element_type_view()
        return self.click(BoardPageElements.type_view_all, type_text)

    def get_type_view_text(self):
        return self.get_element_text(*BoardPageElements.move_to_type_view)

    def select_type_view(self, type_text):
        if type_text == "全 部":
            self.move_to_type_view("全 部")
        elif type_text == "投 票":
            self.move_to_type_view("投 票")
        elif type_text == "活 动":
            self.move_to_type_view("活 动")
        elif type_text == "悬 赏":
            self.move_to_type_view("悬 赏")
        elif type_text == "商 品":
            self.move_to_type_view("商 品")
        elif type_text == "辩 论":
            self.move_to_type_view("辩 论")
        else:
            raise ValueError(
                '''类型选择错误!
                全 部、投 票、活 动、悬 赏、商 品、"辩 论
                '''
            )

    def select_orderway(self, text):
        self.select_by_visible_text(*BoardPageElements.select_orderway, text)

    def get_first_orderway_select_text(self):
        return self.select_first_text(*BoardPageElements.select_orderway)
