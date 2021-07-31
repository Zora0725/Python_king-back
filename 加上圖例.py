# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:35:42 2021

@author: 202107008
"""

import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

seq = [2021, 2022, 2023]
plt.xticks(seq)   # 設定X軸的刻度
plt.plot(seq, Benz, '-*', label = 'Benz')
plt.plot(seq, BMW, '-o', label ='BMW')
plt.plot(seq, Lexus, '-^', label = 'Lexus')
plt.legend(loc='best')   # 圖例
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color='red')
plt.savefig("D:/Python/Figure_1.png", bbox_inches='tight')

plt.show()
