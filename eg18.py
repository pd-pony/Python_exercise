#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg18.py
# @Software: PyCharm
"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编
程找出1000以内的所有完数。
"""
#首先是要找出该数的因子，在判断是否是因子纸盒
list=[]
flag=0
sum=0
for n in range(2,1001):
    k=int(n/2)
    for m in range(1,k+1):
        if n%m==0:
            flag+=1
            list.append(m)
    for i in range(flag):
        sum+=list[i]
    if n==sum:
        print(n)
    flag=0
