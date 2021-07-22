# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:03:49 2021

@author: 202107008
"""

# 可以計算自己花費多少時間猜對數字

import random
import time

min, max = 1, 10
answer = random.randint(min, max)
yourNum = int(input("請猜1-10之間數字 : "))
starttime = int(time.time())
while True:
    if yourNum == answer:
        print("恭喜答對了")
        endtime = int(time.time())
        print("所花時間: ", endtime - starttime, "秒")
        break
    
    elif yourNum < answer:
        print("請猜大一些")
        
    else:
        print("請猜小一點")
    yourNum = int(input("請猜1-10之間的數字: "))
        


    
    