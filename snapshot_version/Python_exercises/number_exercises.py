#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# int 整数
str = '123'
int = int(str)   # 转换int
print(type(int))
intnum = 3  # 直接定义
print(type(intnum))

print(intnum.bit_length())  # 把十进制的3转换成二进制 最少占用位数
newint = intnum.to_bytes(1, 'little')  #1表示用多少个字节表示，little/big,用于指定生成字节的顺序，转为字节
newint1 = intnum.to_bytes(1, 'big')
print(newint)
print(newint1)
print(int.from_bytes(newint, 'little')) #little/big,用于指定生成字节的顺序 转为int

# float 浮点数
str1 = '111'
float = float(str1)  # 转换
floatnum = 3.3  # 直接定义
print(type(float))
print(type(floatnum))
a = floatnum.hex()  # 浮点转十六进制
print(a)
print(float.fromhex(a))   # 十六进制转浮点
print(float.is_integer())  # 判断是不是整数

# bool 布尔型
# complex 复数
a = complex(6,8)
print(a.real)  # 实部
print(a.imag)  # 虚部





