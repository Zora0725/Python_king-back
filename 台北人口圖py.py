# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:43:19 2021

@author: 202107008
"""

import sqlite3
import matplotlib.pyplot as plt
from pylab import mpl

conn = sqlite3.connect("D:/Python/populations.db")
results = conn.execute("SELECT * from population")

area, male, female, total = [],  [], [], []
for record in results:
    area.append(record[0])
    male.append(record[1])
    female.append(record[2])
    total.append(record[3])
conn.close()

mpl.rcParams["font.sans-serif"] = ["SimHei"]
seq = area
linemale, = plt.plot(seq, male, '-*', label="男性人口數")
linefemale, = plt.plot(seq, female, '-o', label="女性人口數")
linetotal, = plt.plt(seq, total, '-^', label="總計人口數")

plt.legend(handles=[linemale, linefemale, linetotal], loc='best')
plt.title(u"台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)
plt.show()

print("--------")
