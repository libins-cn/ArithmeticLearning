# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       most_common_word.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-04-25 23:25
   SoftWare     :       IntelliJ IDEA
   Description  :       最常见的单词[leetcode:819题]
-------------------------------------------------
"""


def most_common_word(paragraph, banned):
    alphabet = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'd', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
                'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', 'a': 'a', 'b': 'b',
                'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p',
                'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}

    words_count = {}

    # 拆分单词

    def load_words(word):
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
        return ""

    # 统计每个单词词频
    word = ""
    for i, a in enumerate(paragraph):
        if a in alphabet and i == len(paragraph) - 1:
            word += alphabet[a]
            word = load_words(word)
            continue
        if a in alphabet:
            word += alphabet[a]
        elif len(word) > 0:
            word = load_words(word)
    # 去掉停用词
    for bnd in banned:
        if bnd in words_count:
            words_count[bnd] = 0

    max_cnt = 0
    max_word = ""
    # 获取出现最大次数的单词
    for word, cnt in words_count.items():
        if cnt > max_cnt:
            max_cnt = cnt
            max_word = word

    return max_word


paragraph = "Bob"
banned = [""]
ret = most_common_word(paragraph, banned)
print(ret)
