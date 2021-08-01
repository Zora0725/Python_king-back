# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:50:03 2021

@author: 202107008
"""

import matplotlib.pyplot as plt
import numpy as np

num = 100
while True:
    x = np.random.random(100)
    y = np.random.random(100)
    t = x
    plt.scatter(x, y, s=100, c=t, cmap='brg')
    plt.show()
    
    Y0Rn = input("是否繼續 (y/n)? ")
    if Y0Rn == 'n' or Y0Rn == 'N':
        break