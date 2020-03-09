# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       repeate_substring_pattern.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-09 22:55
   SoftWare     :       IntelliJ IDEA
   Description  :       重复的子字符串[leetcode:459题]
-------------------------------------------------
"""


# 采用暴力的方法，第一次比较strs[0:1]，第二次比较strs[0:2]...一直到比较strs[0:len(strs) / 2] 个字符串
def repeat_substring_pattern(strs):
    if len(strs) <= 1:
        return False
    i = 0  # 当前已经比到第几个位置了
    pattern = strs[0]  # 初始的模式串只有一个字符
    while len(pattern) <= len(strs) // 2:  # 如果模式串的长度超过字符串的一半，则不用匹配了。肯定是FALSE
        if pattern == strs[i: i + len(pattern)]:  # 判断模式串是否和下一个对应位置长度的字符串相等
            i += len(pattern)  # 更新下一轮比较的开始下标
            if i == len(strs):  # 如果下一轮比较的下标已经是字符串的最后一个元素，则直接返回True
                return True
        else:
            i = 0
            pattern = strs[0: len(pattern) + 1]  # 模式串增加一个字符
    return False


strs = "abcabcabcabc"
ret = repeat_substring_pattern(strs)
print(ret)
