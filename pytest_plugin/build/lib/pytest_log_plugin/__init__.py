#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from typing import List
import os
import logging
import time


# 收集测试用例
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    print("收集用例-----")
    print(items)
    for item in items:
        # 用例名称
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 用例路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    print("收集用例-----")


# 日志初始化
class Logger(object):

    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)  # 进行初始化
        self.logger.setLevel(logging.DEBUG)  # 日志等级为debug
        # 创建一个handler，用于写入日志文件
        # 格式化时间，按照 201712211152 打印
        tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
        if not os.path.exists('./Log'):  # 判断logs文件是否存在
            os.makedirs('./Log')
        log_name = './Log/' + tm + '.log'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s:%(funcName)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        fh.close()
        ch.close()

    def get_log(self):
        return self.logger


logger = Logger(__file__).get_log()