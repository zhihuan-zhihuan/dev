#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import pytest

from dev.pytest_plugin.pytest_log_plugin import logger


def test_log():
    logger.info('我是 info 方法')
    logger.error('我是 error 方法')
    logger.debug('我是 debug 方法')


def test_foo(caplog):
    logger.info('我是 info 方法')
    logger.error('我是 error 方法')
    logger.debug('我是 debug 方法')


@pytest.mark.parametrize("name", ["郝敏", "哈利"])
def test_demo(name):
    logger.info(name)
    logger.debug("demo")
