# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       count_characters.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-17 14:27
   SoftWare     :       IntelliJ IDEA
   Description  :       拼写单词[leetcode:1160]
-------------------------------------------------
"""

# 使用双hash的方式
def count_characters(words, chars):
    mapping = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
               "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for c in chars:
        mapping[c] += 1  # 字母表：每个字母的个数
    output = 0
    for i in range(len(words)):  # 遍历每个单词时初始化一个所有字母都是0个的空字典
        sub_mapping = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0,
                       "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        word_length = 0  # 当前单词能在字母表中查到的个数
        for char in words[i]:  # 如果当前单词在字母表里能够查到，且当前字母已经使用的个数少于字母表里的个数，则视为该字母能查到
            if mapping[char] >= 1 and sub_mapping[char] < mapping[char]:
                word_length += 1
                sub_mapping[char] += 1  # 当前字母的使用个数+1
            else:
                break
        if word_length == len(words[i]):
            output += word_length
    return output


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
ret = count_characters(words, chars)
print(ret)
