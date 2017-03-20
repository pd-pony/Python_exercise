#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg30.py
# @Software: PyCharm
"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""
#类似二分查找的思维
if __name__=='__main__':
    a=[1,3,5,6,8,9,12,23,35,67,89]
    print('the orihinal list is:')
    for i in range(len(a)):
        print(a[i])
    number=int(input('insert a new number'))
    end=a[9]
    if number>end:
        a[10]=number
    else:
        for i in range(10):
            if a[i]>number:
                temp1=a[i]
                a[i]=number
                for j in range(i+1,11):
                    temp2=a[j]
                    a[j]=temp1
                    temp1=temp2
                break
    for i in range(11):
        print(a[i])
