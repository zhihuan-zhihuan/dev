#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import json

import mitmproxy
from mitmproxy import http
from mitmproxy import ctx


class MyProxy:
    """
    对百度首页搜索接口进行map local
    """
    # 对request事件抓包，hook固定写法
    def request(self, flow: mitmproxy.http.HTTPFlow):
        # 判断抓取的flow里的url是否与目标一致
        if 'https://www.baidu.com/sugrec?prod=' in flow.request.pretty_url:
            # pretty_url可转发实现 map remote
            print(f'{flow.request.pretty_url}')
            # 返回body构造，这里可以替换为本地文件，在构造返回时进行read()
            # with open("xxxx.json") as f:
            data = {
                "name": "zhang",
                "age": 19
            }
            # 转json 反序列化
            datas = json.dumps(data)
            # 构造返回
            flow.response = http.HTTPResponse.make(
                200,
                datas
            )
    """
    对百度首页搜索接口进行rewrite，ps：与上面的函数一起使用其实是修改了上面map local的返回
    """
    # 对response事件抓包
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'https://www.baidu.com/sugrec?prod=' in flow.request.pretty_url:
            print(f'{flow.response.text}')
            # 回去响应body，对body序列化,可以直接write()到本地文件里
            data = json.loads(flow.response.text)
            # print(data)
            # 修改返回值
            data["name"] = "zhihuan"
            # 把修改后的响应体反序列化后放回流里去
            flow.response.text = json.dumps(data)

# 插件
addons = [
    MyProxy()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    # 默认端口8080 debug模式： -q 去掉mitmdump日志
    mitmdump(['-s', __file__, '-q'])
