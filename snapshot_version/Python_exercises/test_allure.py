#!/usr/bin/env python
# coding=utf-8

import allure
import pytest


@allure.link('https://docs.pytest.org/en/latest', name='pytest帮助文档')
@allure.issue('http://baidu.com', name='点击我跳转百度')
@allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
def test_other():
    """测试链接，测试链接 ，测试链接"""
    pass
@allure.description('这是一个测试case')
def test_other():
    '''测试链接，测试链接 ，测试链接'''
    pass

list1 = ['full', 'lisa']
@allure.description('这是一个测试case')
@pytest.mark.parametrize('param1', list1)
def test_other(param1):
    print('param1 = ' + param1)
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='点击我看一看youtube吧')
def test_with_named_link():
    pass


@allure.issue('140', 'bug issue链接')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试用例地址')
def test_with_testcase_link():
    pass