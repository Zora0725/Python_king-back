# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:03:27 2021

@author: 202107008
"""

import matplotlib.pyplot as plt
import random

def loc(index):
    x_mov = random.choice([-3, 3])
    xloc = x[index-1] + x_mov
    y_mov = random.choice([-5, -1, 1, 5])
    yloc = y[index-1] + y_mov
    
    x.append(xloc)
    y.append(yloc)
    
    
num = 10000
x = [0]
y = [0]

while True:
    for i in range(1, num):
        loc(i)
        
    t = x
    plt.scatter(x, y, s=2, c=t, cmap='brg')
    plt.show()
    y0Rn = input("是否繼續? (y/n) ")
    if y0Rn == 'n' or y0Rn == 'N':
        break
    else:
        x[0] = x[num-1]
        y[0] = y[num-1]
        del x[1:]
        del y[1:]
        
        