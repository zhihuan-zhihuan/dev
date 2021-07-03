#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: conftest.py
# time: 2021/7/4 6:43 上午
import logging
import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def start_wechat():
    caps = {
            # 设备名称
            "deviceName": "自定义",
            # 手机操作系统
            "platformName": "Android",
            # 操作系统版本
            "platformVersion": "11",
            # Android 应用包名
            "appPackage": "com.tencent.wework",
            # 打开页面
            "appActivity": ".launch.WwMainActivity",
            # 不在会话前重置应用状态
            "noReset": True,
            # 自动同意权限
            "autoGrantPermissions": True,
            # 自动化测试引擎 Appium (默认)
            # 因为appium版本为1.6之前的添加了toast处理需要加UiAutomator2引擎
            "automationName": "UiAutomator2"
        }
    logging.info('添加设备信息')
    # Remote服务
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    # 添加隐式等待保证测试Code的稳定性
    driver.implicitly_wait(10)
    logging.info('启动APP')

    yield driver
    driver.quit()
