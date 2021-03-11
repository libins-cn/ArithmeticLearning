# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		valid_palindrome.py
# CreateDate: 		2021-02-25 19:48:50
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-02-24 19:48:50
# SoftWare:			Visual Studio Code
# Description: 		leetcoee第680题：验证回文字符串II
# -------------------------------------------------
'''

def valid_palindrome(strings):
    def get_flag(strings, t):
        s = 0 # 起始索引
        e = len(strings) - 1 # 终止索引
        cnt = 0 # 是否删除过
        while s <= e:
            if strings[s] == strings[e]: # 首尾相等则通行
                s += 1
                e -= 1
                continue
            if strings[s] != strings[e] and cnt == 1: # 首尾不等，且已经删除过，直接返回本次删除后无法构成非回文
                return 1
            if strings[s] != strings[e] and cnt == 0 and t == 1: # 首尾不等，删除左边那个（左边的索引ID+1）
                s += 1
                cnt += 1
            if strings[s] != strings[e] and cnt == 0 and t == 2: # 首尾不等，删除右边那个
                e -= 1
                cnt += 1
        return 0 # 如果走到这里，说明删除一个元素能够构成回文
    if get_flag(strings, 1) == 0: # 删除左边
        return True 
    if get_flag(strings, 2) == 0: # 删除右边
        return True 
    return False  # 左右两边删除都不能构成回文，则肯定不会构成回文


strings = "aac"
ret = valid_palindrome(strings)
print(ret)