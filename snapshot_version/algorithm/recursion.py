#!/usr/bin/evn python
# -*- coding:utf-8 -*-


def recursion(num):
    # 递归出口
    if num > 0:
        num = num - 1
        print(num)
        # 递归入口
        recursion(num)
        print(num)


recursion(4)
