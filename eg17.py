#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg17.py
# @Software: PyCharm
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如
2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
"""
from functools import reduce
sum=0
list=[]
#注意此处要确定输入的数字类型
n=int(input('n=:\n'))
a=int(input('a=:\n'))
for i in range(n):
    sum=sum+a
    a=a*10
    list.append(a)
    print(a)

list=reduce(lambda  x,y:x+y,list)
print(list)