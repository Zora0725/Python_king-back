# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:55:32 2021

@author: 202107008
"""

# 賭場遊戲騙局

import random
money = 300
bet = 100
min, max = 1, 100
winPercent = int(input("請輸入莊家贏的比率(0-100)之間: "))

while True:
    print(f"歡迎光臨: 目前籌碼金額 {money} 美金")
    print(f"每次賭注 {bet} 美金")
    print("猜大小遊戲 : L or l 代表大，S or s代表小，Q or q結束程式")
    
    customerNum = input("= ")
    if customerNum == "Q" or customerNum == "q":
        break
    
    num = random.randint(min, max)
    if num > winPercent:
        print("恭喜!答對了! \n")
        money += bet
        
    else:
        print("答錯了!請再試一次! \n")
        money -= bet
    if money <= 0:
        break
    
print("歡迎下次再來")
