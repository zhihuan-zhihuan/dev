#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from web_selenium.po.index_page import IndexPage


class TestAddDepartmenr:
    # 初始化驱动并进入首页
    def setup_method(self):
        self.index = IndexPage()

    # 关闭浏览器
    def teardown_method(self):
        self.index.close()

    # 添加部门，获取部门名称进行断言
    def test_add_departmenr(self):
        name = self.index.click_contacts().click_add_party().add_party_with_name().get_party_name()
        print(name)
        assert '致幻1' == name
