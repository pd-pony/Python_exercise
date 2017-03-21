#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg50.py
# @Software: PyCharm
"""
题目：列表使用实例。
"""
#list
#新建列表
list=[10086,'中国移动',[1,2,3,4,5,6]]

#列表长度
print(len(list))

#打印列表
print(list)

#添加元素
list.append('hello world')

print(len(list))
print(list[-1])

#弹出最后一个元素
print(list.pop(1))
print(len(list))
print(list)

