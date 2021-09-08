#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from time import sleep

import yaml
import logging
import pytest
from selenium import webdriver

"""
实现复用浏览器的前提：
1.配置好chrome的环境变量
2.设置debug端口且开启debug窗口 --命令行执行chrome --remote-debugging-port=9222
3.手动登录目标地址
4.code中设置浏览器debug端口
5.code中直接打开目标地址，获得cookies并保持在yaml文件中
"""


# Chrome开启debugging
def remote_Chrome():
    chrome_opts = webdriver.ChromeOptions()
    # 设置debugging地址
    chrome_opts.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=chrome_opts)
    logging.info(f"Chrome debugger address is {chrome_opts.debugger_address}")
    return driver


# 获取登录后的cookies，序列化后放入yaml文件
def get_cookies():
    driver = remote_Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookies = driver.get_cookies()
    logging.info("get cookies success!!")
    logging.info(f"{cookies}")
    with open("./datas/cookies.yaml", "w") as f:
        yaml.safe_dump(cookies, f)


def get_driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope="class")
def login_weixin():
    driver = get_driver()
    driver.get("https://work.weixin.qq.com/login")
    logging.info("get driver and login weixin")
    with open("./datas/cookies.yaml", "r") as f:
        cookies = yaml.safe_load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    logging.info("go to contacts page")
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    driver.maximize_window()
    yield driver
    logging.info("closed Chrome")
    driver.quit()


def test_add_user(login_weixin):
    driver = login_weixin()
    driver.find_element_by_id("menu_contacts").click()
    sleep(1)
    driver.find_element_by_css_selector("#username").send_keys("ldw294452@163.com")
    driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("1")
    driver.find_element_by_css_selector("#memberAdd_phone").send_keys("13175091162")
    ele = driver.find_element_by_xpath(
        '//div[contains(@class,"member_edit_formWrap")]/preceding-sibling::div/a[contains(@class,"js_btn_save")]')
    driver.execute_script("arguments[0].scrollIntoView(true)", ele)
    ele.click()

test_add_user()