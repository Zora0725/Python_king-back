# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:33:11 2021

@author: 202107008
"""

print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end = ".")
print()

print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end = ".")    
    
print("===========================")

scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)
count = 0
for sc in scores:
    count += 1
    print(sc, end = " ")
    if count == 5:
        break

print("===========================")

scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score <30:
        continue
    games += 1
print(f"有{games}場得分超過30分")

print("===========================")

num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:
    print(f"{num}是質數")
else:
    for n in range(2, num):
        if num % n == 0:
            print(f"{num}不是質數")
            break
    else:
        print(f"{num}是質數")

print("===========================")

msg1 = "入機對話專欄，告訴我心事吧，我會重複你告訴我的心事"
msg2 = "輸入q 可以結束對話"
msg = msg1 + '\n' + msg2 + '\n' + '='
input_msg = ''
while input_msg != 'q':
    input_msg = input(msg)
    print(input_msg)

print("===========================")

msg1 = "入機對話專欄，告訴我心事吧，我會重複你告訴我的心事"
msg2 = "輸入q 可以結束對話"
msg = msg1 + '\n' + msg2 + '\n' + '='
input_msg = ''
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':
        print(input_msg)
        
print("===========================")

tuition = 50000
year = 0
while tuition < 60000:
    tuition = int(tuition * 1.05)
    year += 1
print(f"經過{year}年後學費會達到或超過60000元")

print("===========================")

players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)
index = 0
while index < len(players):
    if index == n:
        break
    print(players[index], end = " ")
    index += 1

print("===========================")

