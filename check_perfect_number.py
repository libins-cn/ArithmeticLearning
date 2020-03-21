# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       check_perfect_number.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-21 21:57
   SoftWare     :       IntelliJ IDEA
   Description  :       完美数[leetcode:507]
-------------------------------------------------
"""


# 暴力遍历，感觉应该不会通过，结果一次过
def check_perfect_number(num):
    if num == 1:
        return False
    a = 2  # 除数：从2开始
    csum = 1  # 正因子之和
    while a < num // a:  # 除数小于被开方的值，对于num= 100 ，此处就是a < 10
        if num % a == 0:  # 如果能除尽，则累加两个正因子
            csum += a
            csum += num / a
        a += 1
    if csum == num:
        return True
    return False


num = 33550336
ret = check_perfect_number(num)
print(ret)
