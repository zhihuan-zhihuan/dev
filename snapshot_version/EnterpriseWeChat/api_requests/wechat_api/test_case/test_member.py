#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import json

import pytest
from hamcrest import *
from EnterpriseWeChat.api_requests.wechat_api.api.member_api import WechatMemberApi
from faker import Faker


class TestMemberApi:

    # 添加成员
    def test_add_member(self):
        f = Faker(locale='zh_CN')
        userid = f.numerify()
        name = f.name()
        mobile = f.phone_number()
        datasouce = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1, 2]
        }
        resp = WechatMemberApi().create_member(datasouce)
        ex = 0
        qj = resp.json().get("errcode")
        assert resp.json().get("errmsg") == "created"
        # assertThat断言
        assert_that(ex, equal_to(qj))

    # 查找823
    def test_get_member(self):
        resp = WechatMemberApi().get_member("823")
        assert resp.json().get("errcode") == 0
        assert resp.json().get("errmsg") == "ok"
        # pytest.assume多重断言
        pytest.assume(resp.json().get("errcode") == 0)


    # 修改823
    def test_update_member(self):
        data = {
            "userid": "823"
        }
        resp = WechatMemberApi().update_member(data)
        assert resp.json().get("errcode") == 0
        assert resp.json().get("errmsg") == "updated"

    # 删除823
    def test_delete_member(self):
        resp = WechatMemberApi().delete_member("823")
        assert resp.json().get("errcode") == 0
        assert resp.json().get("errmsg") == "deleted"
