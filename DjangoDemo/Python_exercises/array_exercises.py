#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""
数组：https://docs.python.org/3.5/library/array.html#module-array
"""

import numpy as np
from array import array

abc = array("l",[1,2,3,4])
print(type(abc))
print(abc)
pop=abc.pop(1)
print(pop)
print(abc)
print("-------------------------------")


# 构建一维数组
a = np.array([1, 2, 3])
print(type(a))
print(a)
# 按照下标删除
b=np.delete(a,0)
print(b)

# 构建多维数组
array = np.ndarray([2])
print(type(array))
print(array)