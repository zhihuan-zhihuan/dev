# !/usr/bin python3 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   quick_sort.py
  Description :
  Author :    致幻
  date：     2021/7/19
-------------------------------------------------
"""
"""
快速排序：递归调用归位算法
步骤：78965，目标值7
[7, 8, 9, 6, 5]
[5, 8, 9, 6, 5]
[5, 8, 9, 6, 8]
[5, 6, 9, 6, 8]
[5, 6, 9, 9, 8]
[5, 6, 9, 9, 8]
[5, 6, 9, 9, 8]
[5, 6, 7, 9, 8]
[5, 6, 7, 9, 8]
[5, 6, 7, 8, 8]
[5, 6, 7, 8, 8]
[5, 6, 7, 8, 9]
"""
# 归位算法


def partition(li, left, right):
    tmp = li[left]  # 把第一个值归位，第一个值为目标值
    while left < right:  # 至少有两个元素时进入循环
        while left < right and li[right] >= tmp:  # 从右边开始与目标值比较，如果大于 往前继续找
            right = right - 1  # 往前找，直到left 不小于 right 表示找完了，或者 找到的值小于目标值
        li[left] = li[right]  # 把右边小于目标值的值放在目标值的位置上
        # print(li)
        while left < right and li[left] <= tmp:  # 从左边找，同上
            left = left + 1
        li[right] = li[left]
        # print(li)
    li[left] = tmp  # 目标值归位
    # print(li)
    return left  # 返回第一个归位值下标


def quick_sort(li, left, right):
    if left < right:  # 判断数组至少有两个元素
        mind = partition(li, left, right)  # 获取第一个归位值的下标
        quick_sort(li, left, mind - 1)  # 递归归位值左边的值，再次进行归位
        quick_sort(li, mind + 1, right)  # 递归归位值右边的值，再次进行归位
        # print(li)


li = [7, 8, 9, 6, 5]
print(li)
quick_sort(li, 0, len(li)-1)
print(li)

