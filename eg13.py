#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg13.py
# @Software: PyCharm
"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和
等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三
次方。
"""
#简单数学应用
import math
for n in range(100,1000):
    i=n/100  #百位
    j=(n/10)%10 #十位
    k=n%10   #个位
    if n==i**3+j**3+k**3:   #pow(i,3)+pow(j,3)+pow(k,3):
        print(n)
