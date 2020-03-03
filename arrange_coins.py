# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       arrange_coins.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-03 22:50
   SoftWare     :       IntelliJ IDEA
   Description  :       排列硬币[leetcode: 441题]
-------------------------------------------------
"""


# 用两个指针，一个指针用来标记到第几层，另一个用来标记当前层的最大值，如果n的值比当前层的最大值还大
# 则当前层可以形成完整阶梯
def arrange_coins(n):
    layer = 0  # 初始层为0
    max = 0  # 某一层的最大值
    while max <= n:  # 只要当前层的最大值小于等于输入的n，则当前层可以形成完整阶梯
        layer += 1  # 更新可以形成完整阶梯的层
        max += layer  # 更新下一层的最大值
    return layer - 1  # 因为是从第0层开始比较的，所以需要减回一层


ret = arrange_coins(15000000)
print(ret)
