# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 21:24:33 2021

@author: 202107008
"""

import matplotlib.pyplot as plt

x = [x for x in range(9)]  # 產生串列
sqares = [0, 1, 4, 9, 16, 25, 36, 49, 64]   # Y軸的值
plt.plot(x, sqares)
plt.show()


print("-----------------------")

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)   # 這是Y軸的值
plt.axis([0, 8, 0, 70])   # X軸的刻度0-8, Y軸的刻度0-70
plt.grid()  # 增加隔線
plt.show()

print("-----------------------")

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw = 10)  # 線條寬度調整為10
plt.show()

print("--------------------")

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw = 10)  #squares是Y軸的值，LW調整線條寬度
plt.title("Test Chart")
plt.xlabel("Vaule")
plt.ylabel("Square")
plt.show()

print("--------------------")

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw = 10)  # squares是Y軸的值
plt.title("Test Chart", fontsize = 24)
plt.xlabel("Value", fontsize = 16)
plt.ylabel("Square", fontsize = 16)
plt.show()

print("--------------------")

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw = 10)
plt.title("Test Chart", fontsize = 24)
plt.xlabel("Value", fontsize = 16)
plt.ylabel("Square", fontsize = 16)
plt.tick_params(axis = 'both', labelsize = 12, color = 'red') 
# 設定座標軸的刻度大小、顏色、應用範圍
plt.show()

print("--------------------")

import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 3, 6, 10, 15, 21, 28, 36]
seq = [1,2,3,4,5,6,7,8]
plt.plot(seq, data1, seq, data2)
plt.title("Test Chart", fontsize = 24)
plt.xlabel("X-Value", fontsize = 14)
plt.ylabel("Y-value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 12, color = 'red')  
#設定坐標軸的刻度大小；顏色
plt.show()

print("--------------------")


import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]           # data1線條
data2 = [1, 3, 6, 10, 15, 21, 28, 36]           # data2線條
seq = [1,2,3,4,5,6,7,8]
plt.plot(seq, data1, seq, data2)                # data1&2線條
plt.title("Test Chart", fontsize=24)
plt.xlabel("x-Value", fontsize=14)
plt.ylabel("y-Value", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()


