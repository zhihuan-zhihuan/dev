#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import requests

"""
1.post 没封装 
2.接口依赖没优化 pytest.fixture
3.并发 pytest-xdist 插件 pytest -s -n auto
4.日志和报告logger allure
"""


class BaseApi:
    # 类变量定义
    BASEURL = "https://qyapi.weixin.qq.com/cgi-bin"
    CORPID = "ww83f08c903e9552fd"
    CORPSECRET = "bioRuel7uYEyvQqpcOOrejWDc69WmSWbeI2t3Hr3yas"

    # token成员变量
    def __init__(self):
        self.token = self.get_token()

    # 获取token
    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        resp = requests.get(url, params={"corpid": self.CORPID, "corpsecret": self.CORPSECRET})
        return resp.json().get("access_token")

    # 封装requests.gei
    def send_get(self, url, *args, **kwargs):
        crrent_url = self.BASEURL+url
        return requests.get(crrent_url)




