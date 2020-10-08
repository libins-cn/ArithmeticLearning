# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		reverse_words.py
# CreateDate: 		2020-09-26 22:54:53
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-09-26 22:54:53
# SoftWare:			Visual Studio Code
# Description: 		leetcode第557题【反转字符串中的单词 III】
# -------------------------------------------------
'''


def reverse_words(strings:str) -> str:
        cid = 0
        wid = 0
        result = ""
        strings += " " # 增加一个空格
        for i in range(len(strings)):
            if strings[i] == " ":
                while (wid > cid):
                    result += strings[wid -1]
                    wid -= 1
                if i < len(strings) - 1:
                    result += " "
                wid = i + 1
                cid = i + 1
            else:
                wid += 1
        return result


strings=  "Let's take LeetCode contest"
ret = reverse_words(strings)
print(ret)
