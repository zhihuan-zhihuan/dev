# !/usr/bin python3 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   select_sort.py
  Description :
  Author :    致幻
  date：     2021/7/19
-------------------------------------------------
"""
"""
选择排序：假设一个最小值，遍历里列表，第二个元素开始和第一个比，直到最小的再跟当前的换位子
步骤：依次找最小值
[1, 8, 7, 6, 5]
[1, 8, 7, 6, 5]
[1, 5, 7, 6, 8]
[1, 5, 6, 7, 8]
"""


def select_sort(li):
    for i in range(len(li)-1):
        min_index = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_index]:  # 如果后面的数比min_index小
                min_index = j  # 更新min_index，直到遍历数组内的全部值找到最小的
        li[i], li[min_index] = li[min_index], li[i]  # 把最小的值与当前的值换位置
        print(li)


li = [1, 8, 7, 6, 5]
print(li)
select_sort(li)
print(li)
