# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   FileName     :       days_between_dates.py
   Author       :       libins
   Contact      :       libins810@gmail.com
   CreateDate   :       2020-04-24 23:13
   SoftWare     :       IntelliJ IDEA
   Description  :       日期之间间隔几天[leetcode: 1360题]
-------------------------------------------------
"""


# 开始日期与1971年1月1日相减得到差值num1
# 结束日期与1971年1月1日相减得到差值num2
# 返回（num1 - num2）的绝对值
def days_between_dates(start_date, end_date):
    # 每月有多少天
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # 判断某年是否是闰年
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 1
        return 0

    # 解析输入日期对应的年、月、日
    def get_ymd(date):
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        return int(year), int(month), int(day)

    # 获取输入日期与1971年1月1日的天数
    def get_diff(date):
        year, month, day = get_ymd(date)
        csum = (year - 1971) * 365
        for y in range(1971, year):
            csum += is_leap_year(y)  # 当前年份与1971年之间有几个闰年就加几天
        for m in range(1, month):
            if m == 2 and is_leap_year(year) == 1:  # 如果是2月份，且是闰年，多加一天
                csum += month_days[m] + 1
            else:
                csum += month_days[m]
        return csum + day  # 返回天数

    # 取绝对值
    return abs(get_diff(start_date) - get_diff(end_date))


ret = days_between_dates("2100-04-24", "2020-04-24")
print(ret)
