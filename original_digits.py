# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       original_digits.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-02-29 22:51
   SoftWare     :       IntelliJ IDEA
   Description  :       从英文中重建数字[leetcode: 423题]
-------------------------------------------------
"""


def original_digits(strings):
    # 初始化26个字母每个出现的次数都是0
    hash = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for s in strings:
        hash[s] += 1  # 统计每个字母出现的次数

    nums = [0] * 10  # nums[0]表示0的出现次数，nums[1]表示1的出现次数
    nums[0] = hash['z']  # z只在0中出现
    nums[2] = hash['w']  # w只在2中出现
    nums[4] = hash['u']
    nums[6] = hash['x']
    nums[8] = hash['g']

    nums[3] = hash['h'] - nums[8]  # h 只在3和8中出现
    nums[5] = hash['f'] - nums[4]  # f只在4和5中出现
    nums[7] = hash['s'] - nums[6]  # s只在6和7中出现

    nums[9] = hash['i'] - nums[6] - nums[5] - nums[8]  # i 只在6，9，5，8中出现
    nums[1] = hash['n'] - 2 * nums[9] - nums[7]  # n 只在1，9，7中出现，注意9有两个n

    result = ""
    for i in range(len(nums)):  # 根据每个数字出现的次数组装返回值
        for j in range(nums[i]):
            result += str(i)

    return result


strings = "nnei"
od = original_digits(strings)
print(od)
