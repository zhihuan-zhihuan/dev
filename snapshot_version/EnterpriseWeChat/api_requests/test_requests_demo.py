# !/usr/bin python3 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   test_requests_demo.py
  Description :
  Author :    致幻
  date：     2021/7/15
-------------------------------------------------
"""
import json
from faker import Faker
import requests

f = Faker(locale='zh_CN')


def test_api_wechat():
    corpid = "ww83f08c903e9552fd"
    corpsecret = "bioRuel7uYEyvQqpcOOrejWDc69WmSWbeI2t3Hr3yas"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)
    # print(r.json().get("access_token"))
    token = r.json().get("access_token")
    tager_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
    tagid = f.numerify()
    tagname = f.job()
    print(tagname, tagid)
    data = {
        "tagname": tagname,
        "tagid": tagid
    }
    data = json.dumps(data)
    r = requests.post(tager_url, data)
    # print(r.json().get("tagid"))
    res_tagid = r.json().get("tagid")
    # print(type(tagid), type(res_tagid))
    assert tagid == str(res_tagid)
