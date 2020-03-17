# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_complement.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-16 23:05
   SoftWare     :       IntelliJ IDEA
   Description  :       数字的补数[leetcode:476，1009]
-------------------------------------------------
"""


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        # 利用递归获取该10进制转化为二进制的位数
        def get_bin_nums(num):
            # 递归终止条件
            if num == 0:  # 如果余数为0，则直接返回0位
                return 0
            if num == 1:  # 如果余数是1，则返回1位
                return 1
            num = num // 2
            return get_bin_nums(num) + 1

        # 获取到位数之后，直接取该位数的最大值
        # 比如输入的是5，得到3位，而3位二进制的最大值为（111），换成10进制就是7
        # 我们为了得到7，可以用8-1，也即是2的3次方减一。3怎么来的呢？就是递归求来的
        bin_nums = get_bin_nums(num)
        bin_max = 2 ** bin_nums - 1
        return bin_max - num  # 最后十进制的补码就是对应二进制的最大值减去输入的值
