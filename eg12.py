#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg12.py
# @Software: PyCharm
"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""
#了解素数的定义及判定方法
from math import sqrt
#设置标签
flag=1
num=0
for i in range(101,201):
    #判断是否是素数
    k=int(sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            flag=0
    #如果是素数，则总数加1并输出
    if flag==1:
        num+=1
        print(i)
    #恢复标签
    flag=1

print("the total number is %d"%num)