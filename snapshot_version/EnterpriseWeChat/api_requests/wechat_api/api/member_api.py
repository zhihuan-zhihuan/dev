#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import json
import requests
from EnterpriseWeChat.api_requests.wechat_api.base.base import BaseApi


class WechatMemberApi(BaseApi):

    # 创建接口
    def create_member(self, data):
        url = self.BASEURL+f"/user/create?access_token={self.token}"
        data = json.dumps(data)
        return requests.post(url, data)

    # 查询接口
    def get_member(self, userid):
        url = f"/user/get?access_token={self.token}&userid={userid}"
        return self.send_get(url)

    # 修改接口
    def update_member(self, data):
        url = self.BASEURL+f"/user/update?access_token={self.token}"
        data = json.dumps(data)
        return requests.post(url, json=data)

    # 删除接口
    def delete_member(self, userid):
        url = f"/user/delete?access_token={self.token}&userid={userid}"
        return self.send_get(url)

