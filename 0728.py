# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:06:10 2021

@author: 202107008
"""

import pandas as pd

data_dict = {
    "年度" : range(5),
    "A方案" : [3000, 1900, 1100, 800, 300],
    "B方案" : [3000, 600, 800, 1200, 2000],
    "C方案" : [1500, 500, 1200, 150, 160]}

df = pd.DataFrame(data_dict)
print(df)

# 設定年度欄位當成index
# index限制
# 不能重複
# 必須是不可變的資料型態

df.index = df["年度"]
print(df)
print("--------------")

#取出某個欄位

single_columns = df["年度"]
print(single_columns)
print(type(single_columns))  # 單一欄位取出來Series，等於EXCEL的一個欄位

import pandas as pd

df = pd.read_excel('D:/Python/0050.xlsx')
print(df)
print(df.shape)

print("------------")

print(df.index)
print(list(df.index))

# (20, 9) 代表20列9欄 回傳tuple容器