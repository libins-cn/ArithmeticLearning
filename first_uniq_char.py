# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		first_uniq_char.py
# CreateDate: 		2021-01-03 21:49:14
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-01-03 21:49:14
# SoftWare:			Visual Studio Code
# Description: 		leetcode第387题：字符串中的第一个唯一字符	
# -------------------------------------------------
'''

def first_uniq_char(strings):
    alphas = {}  # 构建一个hash表，存储每个字母出现的次数
    for a in strings:
        if a in alphas:
            alphas[a] += 1
        else:
            alphas[a] = 1
    # 再从头遍历一次原始字符串，当碰到出现次数为1的字母，直接返回索引
    for i in range(len(strings)):
        if alphas[strings[i]] == 1:
            return i
    return -1  # 如果不存在不重复的字母，直接返回-1


strings = "loveleetcode"
ret = first_uniq_char(strings)
print(ret)
