#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# 升序数组的二分查找，升序数组，降序需要改变判断条件


def binary_search(li, tag):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == tag:
            return mid
        if li[mid] > tag:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(binary_search(li, 4))
# print(binary_search(li, 9))
# print(binary_search(li, 11))
# print(binary_search(li, 1))

# 旋转数组二分查找


def binary_search_mojito(li, tag):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == tag:
            return mid
        # 旋转点在右
        if li[mid] >= li[left]:
            if li[left] <= tag < li[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 旋转点在左
        else:
            if li[mid] < tag <= li[right]:
                left = mid + 1
            else:
                right = mid - 1
    else:
        return -1


# li1 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
# li2 = [6, 7, 8, 9, 1, 2, 3, 4, 5]
# li3 = [3, 4, 5, 6, 7, 8, 9, 1, 2]
# print(binary_search_mojito(li1, 8))
# print(binary_search_mojito(li1, 3))
# print(binary_search_mojito(li1, 6))
# print(binary_search_mojito(li1, 11))
# print("----------------")
# print(binary_search_mojito(li2, 8))
# print(binary_search_mojito(li2, 1))
# print(binary_search_mojito(li2, 3))
# print(binary_search_mojito(li2, 11))
# print("----------------")
# print(binary_search_mojito(li3, 4))
# print(binary_search_mojito(li3, 9))
# print(binary_search_mojito(li3, 2))
# print(binary_search_mojito(li3, 11))
