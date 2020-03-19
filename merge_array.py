# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       merge_array.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-19 22:45
   SoftWare     :       IntelliJ IDEA
   Description  :       合并排序的数组[leetcode:面试题10.01]
-------------------------------------------------
"""


# 从最大值开始比较
def merge_array(A, B, m, n):
    i = len(A) - 1  # 从A数组里最后一个元素（最大的元素）开始比较
    while n > 0 and m > 0:
        if B[n - 1] > A[m - 1]:  # 如果B的最后一个元素（B的最大值）大于A的最大值，则把B的这个值放到A的当前位置
            A[i] = B[n - 1]  # 更新B的最最大值索引
            n -= 1
        else:
            A[i] = A[m - 1]  # 反之，把A的最大值放到该位置
            m -= 1  # 更新A的最大值索引
        i -= 1
    for j in range(n):  # 要注意，如果上述循环完后，B里面还有数据，或者B还没有遍历到0，则说明B里面剩下的元素都小于A的最小元素，需要把这些元素放到A
        A[j] = B[j]
    return A


A = [1, 0]
m = 1
B = [1]
n = 1
ret = merge_array(A, B, m, n)
print(ret)
