# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		length_of_last_word.py
# CreateDate: 		2020-07-09 22:47:10
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-09 22:47:10
# SoftWare:			Visual Studio Code
# Description: 		leetcode 58题：最后一个单词的长度	
# -------------------------------------------------
'''

# 从最右边开始往前数，遇到第一个不是空格的地方再开始计数，直到再遇到空格
# 需要注意边界值全为null的情况
def length_of_last_word(s) -> int:
        ret = 0
        id = len(s) - 1
        while  id >= 0 and s[id] == ' ':
            id -= 1
        while id >= 0:
            if s[id] == ' ':
                break
            ret += 1
            id -= 1
        return ret


s = "Hello Worldd"
ret = length_of_last_word(s)
print(ret)
