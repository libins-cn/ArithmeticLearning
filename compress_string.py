# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       compress_string.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-16 14:02
   SoftWare     :       IntelliJ IDEA
   Description  :       字符串压缩[leetcode:面试题01.06]
-------------------------------------------------
"""


def compress_string(input):
    if len(input) <= 2:
        return input
    output = ""
    tmp = [input[0], 1]  # 第一个元素是key，第二个元素计数
    for i in range(1, len(input)):
        if input[i] == tmp[0]:  # 判断当前元素与tmp里的是否一致
            tmp[1] += 1  # 一致的话直接计数器+1
            continue
        output += tmp[0] + str(tmp[1])  # 不一致的话直接把当前tmp里的key和value拼接到output
        tmp[0] = input[i]  # 同时清空tmp里的key和value
        tmp[1] = 1
    output += tmp[0] + str(tmp[1])
    if len(output) >= len(input):
        return input
    return output


strs = "bbbac"
ret = compress_string(strs)
print(ret)
