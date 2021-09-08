#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import pytest


def pytest_addoption(parser):
    mygroup = parser.getgroup("zhihuan")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )


# 如何针对传入的不同参数完成不同的逻辑 处理？ 创建一个fixture，
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env")