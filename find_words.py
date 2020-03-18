# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_words.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-18 23:09
   SoftWare     :       IntelliJ IDEA
   Description  :       键盘行[leetcode:500]
-------------------------------------------------
"""


# 第一行的所有字母类别为1，第二行为2，第三行为3
# 只需要取出每个单词的每个字母所处的类别是否跟第一个单词的相同即可
def find_words(words):
    mapping = {'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1, 'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1,
               'o': 1, 'p': 1, 'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2, 'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2,
               'k': 2, 'l': 2, 'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
    output = []
    for word in words:
        i = 0
        while i < len(word):
            if mapping[word[i]] == mapping[word[0]]:
                i += 1
            else:
                break
        if i == len(word):
            output.append(word)
    return output


words = ['a']
ret = find_words(words)
print(ret)
