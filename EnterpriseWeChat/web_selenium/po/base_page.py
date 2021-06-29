#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化Driver
    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = base_driver

    # 关闭浏览器
    def close(self):
        self.driver.close()

    # 单个元素查找
    def find(self, by, locator) -> WebElement:
        element = self.driver.find_element(by, locator)
        return element

    # 一组元素查找
    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    # 元素查找并点击
    def find_and_click(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()

    # 等待元素可点击
    def wait_for_click(self, by, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, locator)))
        element.click()
