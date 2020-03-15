# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       island_perimeter.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-15 22:44
   SoftWare     :       IntelliJ IDEA
   Description  :       岛屿的周长:[leetcode:463题]
-------------------------------------------------
"""


# 解题思路：依次遍历每个网格的顶点，看该顶点是否是1，如果是1，则再看该顶点的上下左右四个方向相邻的顶点是否是1
# 如果某个方向相邻的元素是1，则说明有公共的边，不计入总周长里
def island_perimeter(grid):
    counter = 0
    flag = 0  # 标记截止当前遍历到的节点中是否有1的，默认没有
    for rid in range(len(grid)):
        lake = 0  # 判断本行数据是否有1
        for cid in range(len(grid[rid])):
            if grid[rid][cid] == 0:
                continue
            flag = 1  # 标记截止当前是否有1的节点产生
            lake = 1  # 标记本行数据是否有1
            # 查看该元素上面的元素是否是岛屿
            if rid == 0 or grid[rid - 1][cid] == 0:
                counter += 1
                # 查看该元素下面的元素是否是岛屿
            if rid == len(grid) - 1 or grid[rid + 1][cid] == 0:
                counter += 1
                # 查看该元素左面的元素是否是岛屿
            if cid == 0 or grid[rid][cid - 1] == 0:
                counter += 1
            # 查看该元素右面的元素是否是岛屿
            if cid == len(grid[rid]) - 1 or grid[rid][cid + 1] == 0:
                counter += 1
        # 如果截止当前已经有岛屿产生，且是本行的数据全是0（lake=0），则下面的数据不用再遍历了，因为题目给了不存在湖的情况
        if flag == 1 and lake == 0:
            return counter
    return counter


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
ret = island_perimeter(grid)
print(ret)
