#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: selectmodulpage.py
# time: 2021/7/4 4:16 上午
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from mobile_test.po.basepage import BasePage
from mobile_test.po.datapage import DataPage


class SelectModulPage(BasePage):
    # 选择手动添加
    def select_manual(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        logging.info('点击手动输入添加按钮')
        return DataPage(self.driver)

    # 获取添加结果
    def toast_assert(self):
        WebDriverWait(self.driver, 10).until\
            (lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        toast_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        logging.info('添加成功获取toast提示')
        # 返回结果
        return toast_text
