# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:26:56 2021

@author: 202107008
"""

files = ['da1.c','da2.py','da3.py','da4.java']
py = []
for file in files:
    if file.endswith('.py'):
        py.append(file)
print(py)


print("===============================")

fruits1 = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
fruits2 = ['香蕉', '芭樂', '西瓜']
print("印出目前fruits2串列", fruits2)
for fruit in fruits2[:]:
    if fruit in fruits1:
        fruits2.remove(fruit)
        print(f"刪除{fruit}")
print("最後fruits2串列", fruits2)

       
print("===============================")


n = int(input("請輸入星號數量"))
for number in range(n):
    print("*",end = " ")
    
print("===============================")

money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print(f"第 {i + 1} 年本金和 : {int(money)}")
    
print("===============================")

n = int(input("請輸入n值: "))
sum = 0
for num in range(1, n+1):
    sum += num
print("總和: ", sum)

print("===============================")

# ch7_14.py
squares = []                     # 建立空串列
n = eval(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    value = num * num            # 元素平方
    squares.append(value)        # 加入串列
print(squares)

print("===============================")

fruits = ["蘋果", "香蕉", "西瓜", "水蜜桃", "百香果"]
print("目前fruits的串列", fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print(f"刪除{fruit}")
    print("目前fruits串列", fruits)
    
print("===============================")

xlst = []
for n in range(6):
    xlst.append(n)
    print(xlst)

print("===============================")

xlst = list(range(6))
print(xlst)

print("===============================")

x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c**2]
print(x)

print("===============================")

colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square", "Line"]
result = [[color,shape] for color in colors for shape in shapes]
print(result)

print("===============================")

colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square"]
result = [[colors, shapes] for color in colors for shape in shapes]
for color,shape in result:
    print(result)
    