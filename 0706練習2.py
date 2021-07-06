# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:03:57 2021

@author: USER
"""

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
i = cars.index(search_str)
print(f"所搜索元素 {search_str} 第一次出現的位置是 {i}")
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print(f"所搜索的元素 {search_val} 第一次出現的位置是{j} ")

###################

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
num1 = cars.count(search_str)
print(f"所搜尋元素 {search_str} 出現{num1} 的次數")

num = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = num.count(search_val)
print(f"所搜尋元素 {search_val} 出現 {num2} 的次數")

#####################

James = [["Leborn Jsmes","SF","12/30/1984"],23,19,22,31,18]
games = len(James)   #計算元素數量
score_Max = max(James[1:games]) #最高得分
i = James.index(score_Max)
Name = James[0][0]
Position = James[0][1]
birth = James[0][2]

print("姓名: ",Name) 
print("位置: ", Position)
print("出生日期: ", birth)
print(f"在第 {i}場得到最高分 {score_Max}")

#另外寫法
Name, Position, birth = James[0]

####################

