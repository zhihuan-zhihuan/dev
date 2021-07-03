#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: basepage.py
# time: 2021/7/4 4:13 上午
from appium import webdriver

class BasePage:
    # 初始化APP
    def __init__(self, driver: webdriver):
        self.driver = driver
