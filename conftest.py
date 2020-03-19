# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 12:53
# @File    : conftest.py
import pytest, os, re, datetime
from selenium import webdriver
from py._xmlgen import html

_driver = None


# 测试失败时添加截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败时，自动截图，并展示到HTML报告
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = os.path.join(os.getcwd(),'report','picture',report.nodeid.replace("::", "_").replace("/", "_") + ".png")
            # file_name_matches = re.findall(r"(\[[\s\S]*\])", file_name)
            # CURRENT_TIME = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
            # file_name = file_name.replace(file_name_matches[0], CURRENT_TIME)
            file_name = report.nodeid.replace("::", "_") + ".png"
            print(file_name)
            screen_img = _capture_screenshot()
            # _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

def _capture_screenshot():
# def _capture_screenshot(file_name):
    """
    截图保存为base64  ///  png
    :return:
    """
    return _driver.get_screenshot_as_base64()
    # return _driver.get_screenshot_as_file(file_name)


# 修改Environment
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "DRV Link"
    config._metadata['接口地址'] = '***********'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


# 修改Summary
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: SVD测试中心")])
    prefix.extend([html.p("测试人员: blake.wang")])

"""
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    # cells.insert(2, html.th('Test_nodeid'))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    # cells.insert(2, html.td(report.nodeid))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)

"""

'''
fixture作用范围
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
- function 每一个函数或方法都会调用
- class  每一个类调用一次，一个类可以有多个方法
- module，每一个.py文件调用一次，该文件内又有多个function和class
- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
'''


@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open browser------------')
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    _driver = webdriver.Chrome(executable_path=r"E:\SoftWare\seleniumdriver\chromedriver.exe", options=options)
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()
