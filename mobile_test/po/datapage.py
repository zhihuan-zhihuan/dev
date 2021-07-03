#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: datapage.py
# time: 2021/7/4 4:17 上午
import logging
import random
from appium.webdriver.common.mobileby import MobileBy
from mobile_test.po.basepage import BasePage



class DataPage(BasePage):

    def add_data(self):
        logging.info('开始添加成员信息')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b09').send_keys('致幻')
        num = random.randint(10000000, 99999999)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/f7y').send_keys(f'131{num}')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ad2').click()
        logging.info('成员信息添加完成')
        from mobile_test.po.selectmodulpage import SelectModulPage
        return SelectModulPage(self.driver)
