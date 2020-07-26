# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		is_palindrome.py
# CreateDate: 		2020-07-15 22:34:27
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-15 22:34:27
# SoftWare:			Visual Studio Code
# Description: 		leetcode 判断回文数	
# -------------------------------------------------
'''


def is_palindrome(x) -> bool:
    strx = str(x)
    h = 0  # 头索引
    t = len(strx) - 1  # 尾索引
    while h <= t:
        if strx[h] == strx[t]:
            h += 1
            t -= 1
            continue
        return False
    return True


x = 0
ret = is_palindrome(x)
print(ret)
