# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       word_pattern.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-06 22:27
   SoftWare     :       IntelliJ IDEA
   Description  :       
-------------------------------------------------
"""


def word_pattern(pattern: str, strs: str):
    def get_flags(strings):
        hash = {}
        n = 1
        flag = ""
        for p in strings:
            if p in hash:
                flag += str(hash[p])
                continue
            hash[p] = n
            flag += str(n)
            n += 1
        return flag

    words = []
    word = ""
    for i in range(len(strs)):
        if i == len(strs) - 1:
            word += strs[i]
            words.append(word)
            break
        elif strs[i] == " ":
            words.append(word)
            word = ""
            continue
        word += strs[i]
    pattern_flag = get_flags(pattern)
    strs_flag = get_flags(words)
    print(pattern_flag)
    print(strs_flag)
    return pattern_flag == strs_flag


pattern = "abcdefghijkaa"
strs = "a b c d e f g h i j a a k"
ret = word_pattern(pattern, strs)
print(ret)
