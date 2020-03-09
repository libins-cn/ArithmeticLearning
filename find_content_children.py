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


#
def find_content_children(g, s):
    if len(g) == 0 or len(s) == 0:
        return 0
    g = sorted(g)
    s = sorted(s)
    counter = 0
    for a in g:
        if len(g) == 0 or len(s) == 0:
            break
        if s[0] >= a:
            counter += 1
            g = g[1:]
            s = s[1:]
        else:
            g = g[1:]
    return counter


g = [1, 2, 3]
s = [1, 1]
ret = find_content_children(g, s)
print(ret)
