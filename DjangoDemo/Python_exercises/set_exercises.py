#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""
集合：https://blog.csdn.net/qq_44034384/article/details/107370950?ops_request_misc=
%257B%2522request%255Fid%2522%253A%2522162278692816780255274026%2522%252C%2522scm%25
22%253A%252220140713.130102334..%2522%257D&request_id=162278692816780255274026&biz_id=
0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-107
370950.first_rank_v2_pc_rank_v29&utm_term
=python%E9%9B%86%E5%90%88%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95&spm=1018.2226.3001.4187
"""
def get_num(num):
    if num > 2:
        get_num(num - 1)
    print(num)


get_num(4) # 输出结果为：2 3 4

# 递归思想
'''
def get_num(4):
    if 4 > 2:
        get_num(4 - 1)
            if 3 > 2:
                get_num(3 - 1)
            print(3)
                    if 2 > 2:
                      pass
                print(2)
    print(4)

递去的num为 432  归来的num为 234
递归，自己调用自己  一个函数
闭包，两个函数相互调用相互返回  两个函数
'''