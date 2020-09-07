# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		detect_capital_use.py
# CreateDate: 		2020-07-28 23:05:25
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-28 23:05:25
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第520题：检测最大的字母	
# -------------------------------------------------
'''

# 1、第一个元素是小写的情况下，只要后面出现一次大写，直接就return false，一直到最后一个元素
# 2、第一个元素是大写，则分为两种情况
#    2.1、如果第二个元素是大写，则以后的元素中只要出现小写，就直接return false
#    2.2、如果第二个元素是小写，则以后出现的元素中只要出现大写，就直接return false
def detect_capital_use(word: str) -> bool:
    upper = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
             "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    lower = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
             "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    if len(word) < 2:
        return True

    if word[0] in upper: # 第一个元素是大写，则分为两种情况
        if word[1] in upper: # 如果第二个元素是大写，则以后的元素中只要出现小写，就直接return false
            for i in range(2, len(word)):
                if word[i] in lower:
                    return False
            return True
        else: # 如果第二个元素是小写，则以后出现的元素中只要出现大写，就直接return false
            for i in range(2, len(word)):
                if word[i] in upper:
                    return False
            return True
    else: # 第一个元素是小写的情况下，只要后面出现一次大写，直接就return false，一直到最后一个元素
        for i in range(1, len(word)):
            if word[i] in upper:
                return False
        return True


word = "FLaG"
ret = detect_capital_use(word)
print(ret)
