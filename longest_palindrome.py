# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       longest_palindrome.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-19 11:25
   SoftWare     :       IntelliJ IDEA
   Description  :       最长回文[leetcode:409]
-------------------------------------------------
"""


# 1、出现偶数次的字母可以全部组成回文
# 2、出现奇数次（比如n次）的字母，只能有n - 1个参与回文的建立，但是最中间的那个字母允许是奇数个
def longest_palindrome(chars):
    mapping = {}
    for c in chars:  # 计算每个字母出现的次数
        if c in mapping:
            mapping[c] += 1
        else:
            mapping[c] = 1
    output = 0  # 输出最终结果
    label = 0  # 判断是否有的字母有奇数个
    for v in mapping.values():  # 遍历所有字母的出现次数
        if v % 2 == 1 and v > 0:  # 如果该字母出现奇数次，则可组成回文的长度为v - 1
            label = 1  # 同时把标记置为1，表示输入的字符串中有字母出现奇数次
            output += (v - 1)
        elif v % 2 == 0:  # 如果该字母出现偶数次，则该字母可以组成回文
            output += v
    return output + label  # 返回总的次数 +1（如果有的字母出现奇数次，则有一个奇数次的字母可以放在最中间）


chars = ""
print(len(chars))
ret = longest_palindrome(chars)
print(ret)
