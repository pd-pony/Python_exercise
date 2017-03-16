#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg16.py
# @Software: PyCharm
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
import string
str=input('input a string:\n')
letters=0
space=0
digit=0
others=0
for c in str:
    #判断是否是字符
    if c.isalpha():
        letters+=1
    #判断是否是空格
    elif c.isspace():
        space+=1
    #判断是否是数字
    elif c.isdigit():
        digit+=1
    #qita
    else:
        others+=1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))