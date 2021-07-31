# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 02:24:59 2021

@author: 202107008
"""

import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500) # 建立500個元素的陣列
ypt1 = np.sin(xpt)
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 色彩預設值0, 1, 0
plt.scatter(xpt, ypt2)
plt.show()

