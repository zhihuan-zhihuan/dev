#!/usr/bin/evn python
# -*- coding:utf-8 -*
# 已知 变量name=list('python')
# 1.打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成-1
# 2.打印第二个-1的索引值
# 3.请在后面插入 插入一个子列表["huo","gE"]
# 4.统计字符h的个数
# 5.将'gE' 修改为"Ge",删除huo元素
# 6.将最新的列表 元素顺序颠倒输出
# 6.将列表里面的所有元素 全部展开为一个列表，例 [1,2,[3,4]] 变成[1,2,3,4]
# 定义变量
"""
list:https://blog.csdn.net/yaoyao4959/article/details/86556342?ops_request_misc=%257B%2522request%2
55Fid%2522%253A%2522162278627316780271552196%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%2
57D&request_id=162278627316780271552196&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~
all~sobaiduend~default-1-86556342.first_rank_v2_pc_rank
_v29&utm_term=python%E5%88%97%E8%A1%A8%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95&spm=1018.2226.3001.4187
"""
name = list('python')
a = [1, 2, 3, 4, 5]
c=map(str,a)
b = list(c)
print(c)
print(b)
print(",".join(b))

