# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:34:51 2021

@author: USER
"""

#if...else練習

age = input("請輸入你的年紀")


if (int(age) < 18):
    print("喔喔~你還未成年!不可購買")
else:
    print("歡迎購買")
        
#####################

#奇數偶數判斷

print("奇數偶數判斷")
num = eval(input("請輸入任意整數"))
rem  = num % 2

if (rem == 0):
    print(f"{num}是偶數")
else:
    print(f"{num}是奇數")
    
if rem:
    print(f"{num} 是奇數")
else:
    print(f"{num} 是偶數")
    
#print(f"{num} 是奇數" if rem else f"{num} 是偶數") 高手寫法

#################

x, y = eval(input("請輸入兩個數字"))
max_ = x if x > y else y
print(f"方法 1最大值是: {max_}")
max_ = max(x, y)
print(f"方法2的最大值是: {max_}")

min_ = x if x < y else y
print(f"方法1最小值是 {min_} ")
min_ = min(x, y)
print(f"方法2最小值是 {min_}")

#######################

items = eval(input("請輸入一個數字:"))
items = 10 if items >= 10 else items
print(items)

######################3#

print("計算最終成績")
score = input("請輸入你的成績")

sc = int(score)
if (sc >=90):
    print("A")
elif (sc >= 80):
    print("B")
elif (sc >= 70):
    print("C")
elif (sc >= 60):
    print("D")
else:
    print("F")
    
    
###################


print("判斷書入字元類別: ")
ch = input("請輸入字元類別")
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("這是大寫字元")
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("這是小寫字元")
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("這是數字")
else:
    print("這是特殊字元")

#################################


#BMI

height = eval(input("請輸入身高"))
weight = eval(input("請輸入體重"))

bmi = weight / (height / 100) ** 2
if bmi >= 28:
    print(f"體重肥胖")
else:
    print(f"體態剛好")

#####################################



    