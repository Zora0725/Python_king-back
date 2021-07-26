# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:39:43 2021

@author: 202107008
"""

def division(x, y):
    try:
        ans = x / y
    except ZeroDivisionError:
        print("除數不可為0")
    else:
        return ans
    
print(division(10, 2))
print(division(5, 0))
print(division(6, 3))

print("--------------------------")

fn = "D:/Python/ch15/ch15_4.txt"
try:
    with open(fn) as file_obj:
        data = file_obj.read()
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    print(data)
    
print("--------------------------")

fn = "D:/Python/ch15/ch15_5.txt"
try:
    with open(fn) as file_obj:
        data = file_obj.read()
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    print(data)
    
print("--------------------------")

fn = "D:/Python/ch15/ch15_6.txt"
try:
    with open(fn) as file_obj:
        data = file_obj.read()
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    wordList = data.split()
    print(f"{fn}文章的字數是 {len(wordList)}")

print("--------------------------")

def wordsNum(fn):
    """適用英文文件，輸入文章的檔案名稱，可以計算此文章的字數"""
    try:
        with open(fn) as file_obj:
            data = file_obj.read()
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
        
    else:
        wordList = data.split()
        print(f"{fn} 文章的字數是 {len(wordList)}")
        
files = ['D:/Python/ch15/data1.txt', 'D:/Python/ch15/data2.txt', 'D:/Python/ch15/data3.txt']
for file in files:
    wordsNum(file)

print("--------------------------")
