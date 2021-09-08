#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""
数组：https://docs.python.org/3.5/library/array.html#module-array
"""

import numpy as np
from array import array

#
# abc = array("l",[1,2,3,4])
# print(type(abc))
# print(abc)
# pop=abc.pop(1)
# print(pop)
# print(abc)
# print("-------------------------------")
#
#
# # 构建一维数组
# a = np.array([1, 2, 3])
# print(type(a))
# print(a)
# # 按照下标删除
# b=np.delete(a,0)
# print(b)
#
# # 构建多维数组
# array = np.ndarray([2])
# print(type(array))
# print(array)
"""
题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
补充说明：
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
"""
# 双循环
# def get_index(nums, target):
#     newnums = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 newnums.append(i)
#                 newnums.append(j)
#     if len(newnums) == 0:
#         print(f"{nums}中没有和为{target}的两个整数")
#     else:
#         print(f"下标为{newnums}")
#
#
# nums = [2, 7, 11, 18]
# target = 9
# get_index(nums, target)
# 减法判断是否在列表中
# def twoSum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         try:
#             other = nums.index(target - nums[i], i + 1)
#         except ValueError as e:
#             continue
#         return [i, other]
# nums = [2, 7, 11, 18]
# target = 11
# print(twoSum(nums, target))

# def getindex(nums, target):
#     for i in range(len(nums)):
#         j = target -nums[i]
#         if j in nums and j != i:
#             return i, nums.index(j)
# nums = [2, 7, 11, 18]
# target = 13
# print(getindex(nums, target))
"""
查看报告的时候前置中显示username_passwd，在步骤中还会再次显示username_passwd，有什么办法取消步骤中的显示吗
"""
# class TestLogin:
#     # 输入账号密码
#     @pytest.fixture()
#     def username_passwd(self):
#         print("username,passworld")
#     # 登录功能
#     @allure.step("登录")
#     def test_login(self, username_passwd):
#         print("login succeed!")
