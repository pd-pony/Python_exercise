#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg53.py
# @Software: PyCharm
"""
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到
一个磁盘文件"test"中保存。
"""
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print (fp.read())
    fp.close()