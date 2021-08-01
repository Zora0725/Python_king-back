# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:29:52 2021

@author: 202107008
"""

import matplotlib.pyplot as plt
import numpy as np

img = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 15, 14, 15]])

plt.imshow(img, cmap = 'Blues')
plt.colorbar()
plt.show()

