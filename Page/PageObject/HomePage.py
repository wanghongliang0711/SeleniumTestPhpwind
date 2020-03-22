"""
@author: wanghongliang
@file: HomePage.py
@time: 2020/3/22 14:55 
"""
from Page.BasePage import BasePage
from config.ElementConfig import HomePageElements
import random

class HomePage(BasePage):
    """首页"""

    def Select_PHPwind_Board(self):
        return self.find_Elements(*HomePageElements.PHPwind_Board)

    def click_PHPwind_Board_by_random(self):
        all_PHPwind_Board = self.Select_PHPwind_Board()
        return all_PHPwind_Board[random.randint(1,len(all_PHPwind_Board))-1].click()

    def go_home(self):
        return self.load_url("http://localhost/phpwind732/")
