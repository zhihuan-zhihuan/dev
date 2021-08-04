#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import pytest

from dev.pytest_plugin.pytest_log_plugin import logger


@pytest.mark.parametrize('a', ['中文', '测试', 'test'], ids=['测试1', '测试2', 'abc'])
def test_a(a):
    logger.info(a)
