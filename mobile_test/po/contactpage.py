#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: contactpage.py
# time: 2021/7/4 4:17 上午
import logging

from appium.webdriver.common.mobileby import MobileBy
from mobile_test.po.basepage import BasePage
from mobile_test.po.selectmodulpage import SelectModulPage


class ContactPage(BasePage):

    def add_member(self):
        # 获取手机宽高尺寸
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        # 通过尺寸坐标向上滑动，保证添加成员按钮可见
        self.driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
        logging.info('向上滑动屏幕')
        # 点击添加成员按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        logging.info('点击添加成员按钮')
        return SelectModulPage(self.driver)
