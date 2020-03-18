# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 11:29
# @File    : conf.py
import os
import datetime

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# 当前时间
CURRENT_TIME = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")

# 报告名称
HTML_NAME = f"testReport{CURRENT_TIME}.html"
