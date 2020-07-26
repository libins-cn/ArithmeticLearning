# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		compress.py
# CreateDate: 		2020-07-20 23:03:45
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-07-20 23:03:45
# SoftWare:			Visual Studio Code
# Description: 		leetcode第443题压缩字符串
# -------------------------------------------------
'''


def compress(chars):
        celem = chars[0] # 当前元素
        cid = 1 # 当前压缩到哪个位置
        rid = 1 # 原始数组当前遍历到哪个位置
        cnum = 1 # 当前元素的当前重复次数
        while rid < len(chars):
            if chars[rid] == celem: # 下一个元素与当前元素相同时，更新计数器的值，更新当前遍历的指针
                cnum += 1
                rid += 1
            else:
                if cnum > 1: # 如果重复次数大1，需要写入数字（先转为字符串再写）
                    cnum_str = str(cnum)
                    for i in cnum_str:
                        chars[cid] = i
                        cid += 1
                    # 写入下一个元素的值
                    chars[cid] = chars[rid]
                    celem = chars[rid] # 更新当前元素为下一个元素
                    cid += 1 # 更新压缩的位置
                    rid += 1 
                    cnum = 1 # 对计数器置1
                else:
                    chars[cid] = chars[rid]
                    celem = chars[rid]
                    cid += 1
                    rid += 1
        # 退出循环后的cid就是压缩长度
        if cnum == 1:
            return len(chars[: cid])
        else: # 如果最后一个元素的cnum大于1，别忘了最后一个元素还需要压缩
            cnum_str = str(cnum)
            for i in cnum_str:
                chars[cid] = i
                cid += 1
            return len(chars[: cid]


chars=["a", "a", "b"]

ret=compress(chars)
print(ret)
