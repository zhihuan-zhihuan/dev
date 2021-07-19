# !/usr/bin python3 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   bubble_sort.py
  Description :
  Author :    致幻
  date：     2021/7/19
-------------------------------------------------
"""
"""
冒泡排序：相邻的两个元素比较比较，大的放后面
步骤：从左往右相邻两个元素比较，大的放后面，每次减去已经排到最后的数
[1, 2, 9, 8, 7, 6, 5]
[1, 2, 8, 9, 7, 6, 5]
[1, 2, 8, 7, 9, 6, 5]
[1, 2, 8, 7, 6, 9, 5]
[1, 2, 8, 7, 6, 5, 9]
[1, 2, 7, 8, 6, 5, 9]
[1, 2, 7, 6, 8, 5, 9]
[1, 2, 7, 6, 5, 8, 9]
[1, 2, 6, 7, 5, 8, 9]
[1, 2, 6, 5, 7, 8, 9]
[1, 2, 5, 6, 7, 8, 9]
"""

def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False  # 标识
        for j in range(len(li) - i - 1):
            # print(len(li)-i-1)  # -i表示减去冒泡到最后的数值
            if li[j] > li[j + 1]:  # 相邻的两个元素比较
                li[j + 1], li[j] = li[j], li[j + 1]  # 排序
                exchange = True  # 前一个数大于后面一个数，状态不变
                print(li)
        if not exchange:  # 前一个数小于后面一个数，不执行上面的if，就没有exchange，然后退出里面的循环
            return


li = [1, 2, 9, 8, 7, 6, 5]
print(li)
bubble_sort(li)
print(li)
