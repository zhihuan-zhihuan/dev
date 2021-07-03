#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: test_add_contact.py
# time: 2021/7/4 4:29 上午
import logging
from mobile_test.po.indexpage import IndexPage



class TestAddContact:

    # TestCase：添加联系
    def test_add_member(self, start_wechat):
        # 获取添加成功的结果
        logging.info('执行用例')
        main = IndexPage(start_wechat)
        result = main.goto_contact().add_member().select_manual().add_data().toast_assert()
        # 断言结果
        assert result == '添加成功'
        logging.info('断言完成')
