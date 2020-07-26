# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		ping_pang.py
# CreateDate: 		2020-07-23 23:26:42
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-23 23:26:42
# SoftWare:			Visual Studio Code
# Description: 		【当当网面试题】乒乓球从200米处往下，落地后都会反弹一半高度，如此反复
#                   请问第10次落地时，一共经过几米？第10次反弹高度是多少？	
# -------------------------------------------------
'''

# 初始高度，反弹次数，反弹次数计数器
def ping_pang(h: int, n: int, cnt: int):
    if cnt >= n:  # 递归终止条件：当反弹次数大于指定次数时，直接返回当前高度
        return h
    cnt += 1
    # 返回经过的路径：当前高度 + 一半高度
    return h + ping_pang(h / 2, n, cnt)


# 测试用例
h = 200  # 初始高度
n = 4  # 反弹次数
cnt = 0  # 反弹次数计数器
ret = ping_pang(h, n, 0)
print(ret)
