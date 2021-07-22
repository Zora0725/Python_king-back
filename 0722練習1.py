# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:44:40 2021

@author: 202107008
"""

# 猜數字遊戲 使用隨機模組
import random

min, max = 1, 10
answer = random.randint(min, max)

while True:
    yourNum = int(input("請輸入1到10之間的數字 : "))
    if yourNum == answer:
        print("恭喜答對了")
        break
    
    elif yourNum < answer:
        print("請猜大一點")
        
    else:
        print("請猜小一點")
        
    
print("===================================")

# 賭場遊戲

import random

min, max = 1, 100
winPercent = int(input("請輸入莊家贏的比率(0-100)之間: "))

while True:
    print("猜大小遊戲: L或l代表大，S or s代表小，Q or q代表程式結束")
    customerNum = input(" = ")   #讀取玩家輸入
    if customerNum == "Q" or customerNum == "q":
        break
    
    num = random.randint(min, max)
    if num > winPercent:
        print("恭喜!答對了! \n")
        
    else:
        print("答錯了!請再試一次! \n")
        
print("===================================")

import  random

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end = ",")
    
print("===================================")

import random

poker = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'J', 'Q', "K", "A"]

for i in range(3):
    random.shuffle(poker)
    print(poker)
    
print("===================================")

# 大樂透

import random

lotterys = random.sample(range(1, 50), 7)
specialNum = lotterys.pop()   # 取特定元素 特別號

print("第XXX期的大樂透號碼", end = " ")
for lottery in sorted(lotterys):    # 排列順序
    print(lottery, end = " ")
    
print(f"\n特別號:{specialNum}")