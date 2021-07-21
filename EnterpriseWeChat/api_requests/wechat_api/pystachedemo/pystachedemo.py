#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import pystache

# python mustache 技术 pystache 练习
demo = pystache.render('Hi,{{person}}!', {'person': 'zhihuan'})
print(demo)
with open("./data.json", mode='r') as f:
    demo1 = pystache.render(f.read(), {'person': 'zhihuan'})
    print(demo1)

with open("./data.json", mode='r') as f:
    demo1 = pystache.render(f.read(), {'person': 'mustache and pystache'})
    print(demo1)