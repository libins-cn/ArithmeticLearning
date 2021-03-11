# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		next_greatest_letter.py
# CreateDate: 		2021-03-11 17:32:48
# Author: 			libins
# Contact:			shenlibin@58.com
# LastModified: 	2021-03-11 17:32:48
# SoftWare:			Visual Studio Code
# Description: 		leetcode第744题：寻找比目标字母大的最小字母	
# -------------------------------------------------
'''


def next_greatest_letter(letters, target):
    words = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,"j": 10,
             "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
             "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    for s in letters:
        if  words[s] > words[target]:
            return s 
    return letters[0]


letters =  ["c", "f", "j"]
target = "k"
ret = next_greatest_letter(letters, target)
print(ret)
