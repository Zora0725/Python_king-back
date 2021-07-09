# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(f"{player.title()}, it was a great game.")
    print(f"我迫不期待想看下一場比賽 {player.title()}")

print("===========================================")

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j} = {result:<3d}", end = " ")
    print()
    
print("===========================================")

print("測試")
for digit in range(1, 10):
    if digit == 5:
        break
    print(digit, end = ".")
print()

print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end = ".")
    