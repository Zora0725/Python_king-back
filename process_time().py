# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:42:14 2021

@author: 202107008
"""

import time

x = 1000000
pi = 0
time.process_time()

for i in range(1, x+1):
    pi += 4*((-1)**(i+1) /(2*i-1))
    if i != 1 and i % 100000 == 0:
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")
        
        # 7d = 7位數的整數  8.7f = 取到小數點第7位
        


