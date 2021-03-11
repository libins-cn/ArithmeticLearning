# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       find_content_children.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-03-06 23:00
   SoftWare     :       IntelliJ IDEA
   Description  :       分发饼干[leetcode: 455题]
-------------------------------------------------
"""


# 饼干和胃口排序，从最小的胃口出发
# 找能满足该胃口的最小饼干
# 如果找到，则记录当前的饼干位置，下一个胃口从此位置开始找合适的饼干
def find_content_children(g, s):
        gs = sorted(g)
        ss = sorted(s)

        si = 0
        result = 0
        for a in gs:
            while si < len(ss):
                if ss[si] >= a:
                    result += 1
                    si += 1
                    break
                si += 1  # 如果当前饼干不足以支持胃口，则继续看下一个饼干
        return result


g = [1, 2, 3]
s = [1, 2]  # 饼


ret = find_content_children(g, s)
print(ret)
