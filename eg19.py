#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg19.py
# @Software: PyCharm
"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
第10次落地时，共经过多少米？第10次反弹多高？
"""
tour=[]
height=[]

hei=100.0#起始高度
time=10#次数

for i in range(1,time+1):
    tour.append(hei)
    hei/=2
    height.append(hei)

print('总高度：tour={0}'.format(sum(tour)))
print('第十次反弹高度：height={0}'.format(height[-1]))

