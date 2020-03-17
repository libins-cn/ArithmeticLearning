# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       license_key_format.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-17 22:40
   SoftWare     :       IntelliJ IDEA
   Description  :       秘钥格式化[leetcode:482题]
-------------------------------------------------
"""


def license_key_format(strs, k):
    if k == 0:
        return 0
    mapping = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N",
               "O": "O", "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "Z", "a": "A", "b": "B",
               "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P",
               "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z", "0": "0", "1": "1", "2": "2", "3": "3",
               "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    label_count = 0
    for s in strs:
        if s == "-":
            label_count += 1
    first_num = (len(strs) - label_count) % k  # 第一个串的长度
    unit_num = (len(strs) - label_count) // k  # 每个串k个字符，算出需要多少个串
    output = ""
    i = 0
    j = 0
    while i < first_num:  # 先统计写入第一个串
        if strs[j] == "-":
            pass
        else:
            output += mapping[strs[j]]
            i += 1
        j += 1
    for z in range(unit_num):  # 写入后序的串
        k_count = 0
        if j > 0:
            output += "-"
        while k_count < k:
            if strs[j] == "-":
                pass
            else:
                output += mapping[strs[j]]
                k_count += 1
            j += 1
    return output


s = "5F3Z-2e-9-w"
k = 0
ret = license_key_format(s, k)
print(ret)
