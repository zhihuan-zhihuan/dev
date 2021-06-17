#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# 定义变量
name = " huogewozi "
# 1. 请去除两边的空格
# 方法一 strip()函数
new_name = name.strip()
print('去除空格方法一：'+ new_name)
#方法二 replace()函数
str_name = name.replace(' ', '')
print(f'去除空格方法二：{str_name}')
# 2.将字符串中的o替换为K
new_namestr = new_name.replace('o', 'K')
print('替换后：{0}' .format(new_namestr))
# 字面量插值
print('替换后：%s' % new_namestr)
# 3.在判断是否以Hu开头和"i"结尾
# 4.如果是 请输出 Ok,否则输出fail
# 方法一
if new_namestr[0:2] == 'Hu' and new_namestr == 'i':
    print('通过下标判断开头结尾是否正确，方法一：OK')
else:
    print('通过下标判断开头结尾是否正确，方法一：fail')

# 方法二
if new_namestr.endswith('i') is True and new_namestr.startswith('Hu') is True:
    print('判断开头结尾是否正确，方法二：OK')
else:
    print('判断开头结尾是否正确，方法二：fail')



a = "dlrblist"
a1 = ",".join(a)
print(a1)

#定义一个函数，用来去除字符串首尾的空格
def trim(string):
    if len(string) == 0:
        return string
    elif string[0] == ' ':
        return (trim(string[1:]))
    elif string[-1] == ' ':
        return (trim(string[:-1]))
    return string



