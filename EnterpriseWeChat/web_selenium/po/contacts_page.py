#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.by import By
from web_selenium.po.base_page import BasePage
from web_selenium.po.department_page import DepartmentPage


class ContactsPage(BasePage):
    _PLUS_ICON = (By.CLASS_NAME, 'member_colLeft_top_addBtn')
    _CREATE_PARTY = (By.CLASS_NAME, 'js_create_party')
    _PARTY_NAME = (By.ID, 'party_name')

    # 点击’+‘，点击添加部门按钮跳转到部门添加页
    def click_add_party(self):
        self.find_and_click(*self._PLUS_ICON)
        self.find_and_click(*self._CREATE_PARTY)
        return DepartmentPage(self.driver)

    # 获取部门名称
    def get_party_name(self):
        # 等待动画结束
        time.sleep(2)
        return self.find(*self._PARTY_NAME).text
