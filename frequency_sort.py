# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       frequency_sort.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-05 22:13
   SoftWare     :       IntelliJ IDEA
   Description  :       根据字符出现频率排序[leetcode:451题]
-------------------------------------------------
"""


# 双hash表的方式
def frequency_sort(chars):
    hash = {}  # 标记每个字符出现的次数，k是字符，v是次数
    for c in chars:
        if c in hash:
            hash[c] += 1
            continue
        hash[c] = 1
    # 标记出现某次的字符有哪些，k是次数，v是对应的字符。比如出现2次的有b,c
    # 则k是2，v是：bbcc
    hash_count = {}
    for k, v in hash.items():
        if v in hash_count:
            hash_count[v] += k * v
            continue
        hash_count[v] = k * v
    result = ''  # 返回结果
    i = len(chars)  # 假设极端情况，某个输入的字符串里每个字符都是一样的，所以从最大次数开始遍历
    while i > 0:
        if i in hash_count:
            result += hash_count[i]
            # 如果result的长度已经超过原始长度了。没有必要再遍历下去。
            # 当重复的字符很多时，可以减少代码运行时间
        if len(result) >= len(chars):
            break
        i -= 1  # 当前次数的字符遍历完了，继续寻找出现次数更低的字符
    return result


chars = ""
ret = frequency_sort(chars)
print(ret)
