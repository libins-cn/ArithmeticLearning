# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       count_segments.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-03 21:47
   SoftWare     :       IntelliJ IDEA
   Description  :       字符串中的单词数[leetcode: 434题]
-------------------------------------------------
"""


# 整体思路就是：判断当前字符不是空白，且上一个字符是空白的情况有多少个。
# 需要注意下第1个字符，所以从1开始遍历
def count_segments(s):
    if len(s) == 0:
        return 0
    count = 0
    if s[0] != " ":  # 如果第一个字符是非空字符，则说明至少有一个单词
        count = 1
    for i in range(1, len(s)):
        if s[i - 1] == " " and s[i] != " ": # 当前字符是非空且上一个字符是空
            count += 1
    return count


s = ""
ret = count_segments(s)
print(ret)
