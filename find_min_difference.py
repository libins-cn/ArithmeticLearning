# -*- coding:utf-8 -*-
'''
# -------------------------------------------------
# FileName: 		find_min_difference.py
# CreateDate: 		2020-09-19 22:44:53
# Author: 			libins
# Contact:			libins.cn@gmail.com
# LastModified: 	2020-09-19 22:44:53
# SoftWare:			Visual Studio Code
# Description: 		leetcode第539题：最小时间差	
# -------------------------------------------------
'''
# 一天只有1440分钟，如果所给的元素超过1440个，则肯定有重复的时间，只要有重复的时间，最小时间差肯定是0
# 如果时间差大于最大的时间差（12小时），说明从另一个方向时间差更小。比如：01：00 与16：00，时间差并不是16小时，而是24 - (16 - 1) = 9小时
# 不要忽略最早时间与最晚时间的时间查，比如：00：00 与23：59分其实是连续的
def find_min_difference(time_points: list) -> int:
    # 获取每个时间点的索引
    def get_index(time_point: str) -> int:
        hour = int(time_point.split(":")[0])
        minute = int(time_point.split(":")[1])
        return hour * 60 + minute

    time_line = [0] * 24 * 60  # 24小时总共有24 * 60 分钟，每分钟对应数组的一个元素
    max_diff = (24 * 60) / 2  # 最大时间差是12小时（720分钟）

    # 将所给的时间对应的索引位置置为1，如果有相同的时间，则索引相同，时间差为0，直接返回
    for time_point in time_points:
        if time_line[get_index(time_point)] == 1:
            return 0
        time_line[get_index(time_point)] = 1

    min_diff = max_diff  # 假设时间差为最大值（720分钟）
    # 从时间线中，找到第一个有时间的位置
    for i in range(len(time_line)):
        if time_line[i] == 1:
            cid = i
            break
    start = cid
    for idx in range(cid + 1, len(time_line)):
        if time_line[idx] == 1:
            if idx - cid >= max_diff:
                # 如果时间差大于最大的时间差，说明从另一个方向时间差更小
                # 比如：01：00 与16：00，时间差并不是16小时，而是24 - (16 - 1) = 9小时
                diff = len(time_line) - (idx - cid)
            else:
                diff = idx - cid
            cid = idx  # 给当前ID赋值，继续与时间线里有时间的下一个时间求差值

            if diff < min_diff:
                min_diff = diff
    # 最后千万不要忽略了，时间线里的第一个时间和最后一个时间做时间差（比如：00：00与23：59分）
    if len(time_line) + start - cid < min_diff:
        return len(time_line) + start - cid
    return int(min_diff)


time_points = ["23:59", "22:59", "23:05"]
ret = find_min_difference(time_points)
print(ret)
