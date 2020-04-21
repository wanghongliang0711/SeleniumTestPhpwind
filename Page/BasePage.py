# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 13:51
# @File    : BasePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""

    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = timeout

    def find_Elements(self, by, locator):
        """
        显示等待 find group elements
        :param by: id, name, xpath, class_name, link_text
        :param locator: id, name, xpath for str
        :return: elements object
        """
        try:
            print(f'Info:Starting find the elements "{locator}" by "{by}"!')
            elements = WebDriverWait(self.driver, self.outTime).\
                until(EC.presence_of_all_elements_located((self.byDic[by], locator)))
        except Exception as e:
            print(f"find_Elements error found, elements:{locator}", e)
        else:
            return elements

    def find_Element(self, by, locator):
        """
        显示等待 find alone element
        :param by: id, name, xpath, class_name, link_text
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            print(f'Info:Starting find the element "{locator}" by "{by}"!')
            element = WebDriverWait(self.driver, self.outTime).\
                until(EC.presence_of_element_located((self.byDic[by], locator)))
        except Exception as e:
            print(f"find_Element error found, element:{locator}", e)
        else:
            return element

    def load_url(self, url):
        """加载url"""
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!')

    def is_click(self, by, locator):
        """判断是否可以点击"""
        try:
            element = WebDriverWait(self.driver, self.outTime).\
                until(EC.element_to_be_clickable((self.byDic[by], locator)))
        except Exception as e:
            print(f"is_click error found, element:{locator}", e)
        else:
            return element

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        try:
            print('info:switching to iframe "{}"'.format(locator))
            WebDriverWait(self.driver, self.outTime).\
                until(EC.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
        except Exception as e:
            print(f"switch_to_frame error found, element:{locator}", e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_Element(by, locator)
            element.clear()
        except Exception as e:
            print(f"clear error found, element:{locator}", e)

    def send_keys(self, by, locator, value=''):
        """写数据"""
        try:
            print(f'info:input "{value}')
            element = self.find_Element(by, locator)
            element.send_keys(value)
        except Exception as e:
            print(f"send_keys error found, element:{locator}", e)

    def switch_to_default_frame(self):
        """返回默认的frame"""
        try:
            print('info:switch back to default iframe')
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"switch_to_default_frame error found.", e)

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_Element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except Exception as e:
            print(f"get_element_text error found, element:{locator}", e)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return WebDriverWait(self.driver, self.outTime).\
                until(EC.visibility_of_element_located((self.byDic[by], locator)))
        except Exception as t:
            print('error: found "{}" timeout！'.format(locator), t)

    def move_to_element(self, by, locator):
        print('info:move_to_element "{}" to be located'.format(locator))
        try:
            element = self.find_Element(by, locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            print(f"move_to_element error found, element:{locator}", e)

    # 移动页面
    def move_page(self, x, y):
        print(f'info:move_page x--> "{x}"  y-->"{y}"')
        try:
            self.driver.execute_script('window.scrollBy(0,600)')
        except Exception as e:
            print(f"move_page error. ", e)


    def select_by_visible_text(self, by, locator, text):
        print('info:select_by_visible_text "{}" to be located'.format(locator))
        try:
            element = self.find_Element(by, locator)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            print(f"select_by_visible_text error found, element:{locator}", e)

    def select_first_text(self, by, locator):
        print('info:select_first_text "{}" to be located'.format(locator))
        try:
            element = self.find_Element(by, locator)
            return Select(element).first_selected_option.text
        except Exception as e:
            print(f"select_first_text error found, element:{locator}", e)