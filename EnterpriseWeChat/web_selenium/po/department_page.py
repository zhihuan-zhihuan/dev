#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from EnterpriseWeChat.web_selenium.po.base_page import BasePage


class DepartmentPage(BasePage):
    _PARTY_NAME = (By.NAME, "name")
    _PARTY_LIST = (By.CLASS_NAME, "js_toggle_party_list")
    _PARTY_ROOT = (By.ID, "1688850876979083_anchor")
    _PARENT_PARTY_TEXT = (By.LINK_TEXT, "{}")
    _CONFIRM = (By.LINK_TEXT, "确定")

    # 填写部门信息，提交后返回通讯录页
    def add_party_with_name(self, parent_party_name=None):
        self.find(*self._PARTY_NAME).send_keys('致幻1')
        self.find_and_click(*self._PARTY_LIST)
        # 判断下拉框里是否有部门选项
        if not parent_party_name:
            self.finds(*self._PARTY_ROOT)[1].click()
        else:
            self.finds(By.LINK_TEXT, parent_party_name)[1].click()
        self.find(*self._CONFIRM).click()
        from web_selenium.po.contacts_page import ContactsPage
        return ContactsPage(self.driver)
