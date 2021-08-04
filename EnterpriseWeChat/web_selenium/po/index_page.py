#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from EnterpriseWeChat.web_selenium.po.base_page import BasePage
from EnterpriseWeChat.web_selenium.po.contacts_page import ContactsPage


class IndexPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    # 点击通讯录跳转到通讯录页面
    def click_contacts(self):
        self.find_and_click(*self._CONTACT)
        return ContactsPage(self.driver)
