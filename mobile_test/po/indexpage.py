#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: indexpage.py
# time: 2021/7/4 4:13 上午
import logging

from appium.webdriver.common.mobileby import MobileBy
from mobile_test.po.basepage import BasePage
from mobile_test.po.contactpage import ContactPage

# 集成基础类获取驱动
class IndexPage(BasePage):
    # 点击通讯录按钮
    def goto_contact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        logging.info('点击通讯录按钮')
        # 返回下个页面，传递驱动信息
        return ContactPage(self.driver)
