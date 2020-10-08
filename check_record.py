# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		check_record.py
# CreateDate: 		2020-09-20 22:30:26
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-09-20 22:30:27
# SoftWare:			Visual Studio Code
# Description: 		leetcode第551题 学生出勤记录	
# -------------------------------------------------
'''

# 的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
def check_record(strings: str) -> bool:
    numa = 0
    numl = 0
    late_flag = 0
    for s in strings:
        if numa > 1 or late_flag > 2:
            return False
        if s == "A":
            numa += 1
            late_flag = 0
            continue
        if s == "L":
            numl += 1
            late_flag += 1
            continue
        late_flag = 0

    if numa > 1 or late_flag > 2:
        return False
    return True


strings = "LPLPLPLPLPL"
ret = check_record(strings)
print(ret)
