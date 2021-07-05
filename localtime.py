# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:00:31 2021

@author: USER
"""

import random

list1 = random.sample(range(1,50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為:", end="")

for i in range(6):
    if i == 5: print(str(list1[i]))
else: print(str(list1[i]), end="")
print("本期大樂透特別號為:" + str(special))

#################

import time

time.time()
import time as t

week = ["一","二","三","四","五","六","日"]
dst = ["無日光節約時間","有日光節約時間"]
time1 = t.localtime()
show = "現在時刻:中華民國 " + str(int(time1.tm_year)-1911) +"年 "
show += str(time1.tm_mon) + "月" + str(time1.tm_mday) + "日"
show += str(time1.tm_hour) + "點" + str(time1.tm_min) + "分" 
show += str(time1.tm_sec) + "秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第" + str(time1.tm_yday) + "天，此地" + dst[time1.tm_isdst]

print(show)

###########################

