#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
int
bit_length
to_bytes(1,'little')
from_bytes(1,'big')
浮点
hex
fromhex
is_integer
复数
real
imag
字符串
capitalize 首字母大写
casefold  转换小写
lower     ascll转换小写
islower   是否小写
upper     转换大写
isupper   是否大写
swapcase  大小写转换
center    两边填充，默认空格 宽度包含字符
rjust     右边填充，默认空格 宽度包含字符
ljust     左边填充，默认空格 宽度包含字符
zfill     （+，-）开头，则在符号之后进行填充。 如果指定的宽度小于原始字符串，则返回原始字符串，填充0 宽度包含字符
strip     去除
rstrip    右开始去除，加下标
join      每个元素添加符号
expandtabs 空格来扩展空间
replace  替换
split    切割
rsplit
splitlines
format
format.map {}
partition 指定分隔符将字符串进行分割，返回三元组
rpartition
title
count
index
rindex
find
rfind
startswith
endswith
列表
append
index
pop
remove
insert
extend
reverse
sort
元组
count
list
tuple
max
min
cmp
len
字典
dict.keys
dict.values
dict.items
dict.clear
dict.copy
dict.updata
dict.pop(keys)
dict.get(keys)
集合
set.issubset
set.issuperset
set.union
set.intersection
set.difference
set.symmetric_difference
set.cop
'''

# import copy
#
# list1 = [1, 2, 3, [4, 5], 7]
# list2 = list1
# list3 = copy.copy(list1)
# list4 = list1[:]
# list5 = copy.deepcopy(list1)
# list1.append(8)
# list1[3].append(6)
# list1.reverse()
# list1[2].reverse()
#
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)

# strs = []
# print(len(strs))
# if len(strs) == 0:
#     print("0")
# else:
#     print("1")
import os
path = os.path.abspath(__file__)
print(path)
path1 = os.path.dirname(__file__)
print(path1)
path2 = os.path.dirname(os.path.abspath(__file__))
print(path2)
path3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path3)
path4 = os.path.abspath('..')
print(path4)