#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import os
from flask import Flask
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)


@app.route('/', methods=['get'])
# 读取yaml文件的接口描述定义
@swag_from(os.path.abspath('..') + "/flaskdemo/get_token.yaml")
def get_token():
    return {'ab': 'ab'}


if __name__ == '__main__':
    app.run(debug=True, port=9898)
    # 访问http://127.0.0.1:9898/apidocs进入接口文档
