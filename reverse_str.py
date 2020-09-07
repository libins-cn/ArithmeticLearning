# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		reverse_str.py
# CreateDate: 		2020-08-03 22:18:19
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-08-03 22:18:19
# SoftWare:			Visual Studio Code
# Description: 		LeetCode第541题：反转字符串||	
# -------------------------------------------------
'''


def reverse_str(s: str, k: int) -> int:
    double_k = 2 * k
    # 获取最后一个区间的起始ID
    last_id = int(len(s) / double_k) * double_k

    # 余数是多少
    remainder = len(s) % double_k

    result = ""  # 最终返回的结果

    # 对每个2k区间内的元素进行交换重写
    def exchange(result, curid, region_max_id):
        region_id = curid + k - 1
        while region_id >= curid:
            result += s[region_id]
            region_id -= 1

        region_id = curid + k
        while region_id < region_max_id:
            result += s[region_id]
            region_id += 1
        return result

    curid = 0
    while curid < last_id:
        result = exchange(result, curid, curid + double_k)
        curid += double_k
    # 处理最后一段区间
    if remainder <= k:
        region_id = last_id + remainder - 1
        while region_id >= last_id:
            result += s[region_id]
            region_id -= 1
    else:
        result = exchange(result, last_id, last_id + remainder)
    return result


s = "abcdefg"
k = 3
ret = reverse_str(s, k)
print(ret)
