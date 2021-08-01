# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:29:54 2021

@author: 202107008
"""

import matplotlib.pyplot as plt
import numpy as np

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)

plt.plot(x, y)
plt.fill_between(x, 0, y, color="green", alpha=0.1)
plt.show()
