# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:00:25 2021

@author: USER
"""

#設計人體體重健康判斷程式

height = eval(input("請輸入你的身高(公分)"))
weight = eval(input("請輸入你的體重(公斤)"))
bmi = weight / (height / 100) ** 2
if bmi >= 18.5 and bmi < 24:
    print(f"{bmi = :5.2f}體重正常")

else:
    print(f"{bmi = :5.2f}體重不正常") 

#猜數字遊戲

ans = 0
print("猜數字遊戲，請心中想一個0-7之間的數字，然後回答問題")

truefalse = "輸入Y或y代表有，其他代表無: "
q1 = "有沒有看到心中的數字:  \n" + \
     "1, 3, 5, 7 \n"

num = input(q1 + truefalse)
print(num)
if num == "Y" or num == "y":
    ans += 1

truefalsue = "輸入Y或y代表有，其他代表無: "
q2  = "有沒有看到心中的數字: \n" + \
    "2, 3, 6, 7 \n"
rum = input(q2 + truefalse)
if num == "Y" or num == "y":
    ans += 2
truefalse = "輸入Y或y代表有，其他代表無: "
q3 = "有沒有看到心中的數字: \n" + \
     "4, 5, 6, 7 \n"
num = input(q3 + truefalse)
if num == "Y" or num == "y":
    ans += 4

print("讀者心中所想的數字是: " , ans)

##################

#生肖系統

year = eval(input("請輸入西元出生年: "))
year -= 1900
zodiac = year % 12
if zodiac == 0:
    print("你的生肖是鼠")
elif zodiac == 1:
    print("你的生肖是牛")
elif zodiac == 2:
    print("你的生肖是虎")
elif zodiac == 3:
    print("你的生肖是兔")

elif zodiac == 4:
    print("你的生肖是龍")
elif zodiac == 5:
    print("你的生肖是蛇")
elif zodiac == 6:
    print("你的生肖是馬")
elif zodiac == 7:
    print("你的生肖是羊")
elif zodiac == 8:
    print("你的生肖是猴")
elif zodiac == 9:
    print("你的生肖是雞")
elif zodiac == 10:
    print("你的生肖是狗")
else:
    print("你的生肖是豬")
    

    