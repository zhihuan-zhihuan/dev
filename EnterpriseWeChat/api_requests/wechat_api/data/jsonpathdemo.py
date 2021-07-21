#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import json

from jsonpath import jsonpath


with open("./data.json", mode="r") as f:
    data = json.load(f)
    print(data)
    print(jsonpath(data, "$.store.book[0:3:2].title"))  # 按步长取，到第1个和第3本书的titile

    print(jsonpath(data, "$.store.book[0:2:2].title"))  # 按步长取到第1本书的titile

    print(jsonpath(data, "$.store.book[?(@.price < 10)].title"))  # 取价格小于10的书的title

    print(jsonpath(data, "$..store.book[(@.length -1)].title"))  # 取最后一本书的title
