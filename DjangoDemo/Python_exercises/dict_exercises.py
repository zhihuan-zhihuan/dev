#!/usr/bin/evn python
# -*- coding:utf-8 -*-

"""
字典：https://blog.csdn.net/haoxun11/article/details/105206601?ops_request_misc=
%257B%2522request%255Fid%2522%253A%2522162278691916780274189975%2522%252C%2522
scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162278691916780274
189975&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~
sobaiduend~default-1-105206601.first_rank_v2_pc_rank_v29&utm_term=
python%E5%AD%97%E5%85%B8%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95&spm=1018.2226.3001.4187
"""
'''
有字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能：

1、遍历字典 dic 中所有的key


2、遍历字典 dic 中所有的value


3、循环遍历字典 dic 中所有的key和value


4、添加一个键值对"k4","v4",输出添加后的字典 dic


5、删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic


6、删除字典 dic 中 'k5' 对应的值，若不存在，使其不报错，并返回None


7、获取字典 dic 中“k2”对应的值


8、获取字典 dic 中"k6"对应的值，如果不存在，使其不报错，并且让其返回数据 None


9、有字典 dic2 = {'k1':"v111",'a':"b"} 通过一行操作使 dic2 = {'k1':"v111",'k2':"v2",'k3':"v3",'k4': 'v4','a':"b"}


10、组合嵌套，实现功能，现有列表如下：

list = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]

（1）将列表中的‘tt’变成大写(两种方式)

 

（2）将数字 3 变成字符串 ‘100’(两种方式)



（3）将列表中的字符串‘1’变成数字101(两种方式)


11、按照要求实现以下功能：li = [1,2,3,'a','b',4,'c']，有一个字典(此字典是动态生成的，你并不知道它有多少键值对，所以用 dic={} 模拟)，具体操作如下：如果字典没有'k1'这个键，那就创建这个'k1'键和对应的值(对应值设为空列表)，并将列表li中的索引为奇数对应的元素，添加到'k1'这个键对应的空列表中；如果有'k1'这个键，且'k1'对应的value值是列表类型，那就将列表li中的索引为奇数对应的元素，添加到'k1'这个键对应的值中。

'''

# import itertools
#
# test = [
#     {'fQY': 'A', 'fWD_MC': 'a1'},
#     {'fQY': 'A', 'fWD_MC': 'a2'},
#     {'fQY': 'A', 'fWD_MC': 'a3'},
#     {'fQY': 'B', 'fWD_MC': 'b1'},
#     {'fQY': 'C', 'fWD_MC': 'c1'},
#     {'fQY': 'C', 'fWD_MC': 'c2'}]
# for i in range(len(test)):
#     test[i].update(name=test[i].pop('fQY'))
#     test[i].update(children=test[i].pop('fWD_MC'))
#
# for name, values in itertools.groupby(test, key=lambda x: x["name"]):
#     data = list(list(values))
#     print(data)
#     print(test)

data = {
    "name": "zhang",
    "age": 12
}

value = data["name"]
print(value)