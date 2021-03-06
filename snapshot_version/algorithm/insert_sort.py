# !/usr/bin python3 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   insert_sort.py
  Description :
  Author :    致幻
  date：     2021/7/19
-------------------------------------------------
"""
"""
插入排序：已有值与获取值比较
步骤：目标值与已有值依次比较，如果目标值大，放在已有值后，如果目标值小，一直往前比较，直到比完还没找到就在当前位置插入
[1, 8, 7, 6, 5]
[1, 8, 7, 6, 5]
[1, 7, 8, 6, 5]
[1, 6, 7, 8, 5]
[1, 5, 6, 7, 8]
[1, 5, 6, 7, 8]
"""


def insert_sort(li):
    for i in range(1, len(li)):  # 第二个数开始到最后一个数
        tmp = li[i]  # 每次获取一个【第二个数开始到最后一个数】的数
        j = i - 1  # 已有的数的下标
        while j >= 0 and li[j] > tmp:  # 判断列表长度和当前已有数和获取数的大小
            li[j + 1] = li[j]  # 已有数向后移动一格，占据获取元素的位子
            j = j - 1  # 下标左移后比较前面的数是否大于获取的数，如果大于，再往后移动一格，J再次-1去比较
            # 直到j<0或者小于获取的数，把获取的值放在这时值的后面
        li[j + 1] = tmp  # 把获取的值放在当前位置
        print(li)


li = [1, 8, 7, 6, 5]
print(li)
insert_sort(li)
print(li)
