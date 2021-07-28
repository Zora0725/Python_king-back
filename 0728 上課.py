# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:25:04 2021

@author: 202107008
"""
# =============================================================================
# 
# import datetime
# 
# today = datetime.datetime.now()
# print(today)
# 
# print(datetime.datetime.timestamp(today))
# 
# 
# =============================================================================

# ctrl + 4 區塊註解
# =============================================================================
# 
# # 請讀取0050.xlsx
# # 新增一個欄位"今日蝶漲幅"，是以"開盤價" - 收盤價來計算
# # 新篩選 今日漲跌幅 > 0 的資料
# 
# import pandas as pd
# 
# df = pd.read_excel("D:/Python/0050.xlsx")
# 
# df["今日漲跌幅"] = df["收盤價"] - df["開盤價"]
# 
# result = df[ df["今日漲跌幅"] > 0 ]
# print(result["今日漲跌幅"])
# =============================================================================

import webbrowser

address = input("請輸入地址")
webbrowser.open('https://www.google.com.tw/maps/place/' + address)

print("--------------------------------")

import requests

url = 'https://www.104.com.tw/jobs/main/'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:ㄦ
    print("取得網站內容成功")
    
else:
    print(" 取得失敗")
