# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:43:10 2021

@author: 202107008
"""

X = frozenset([1, 3, 5])
Y = frozenset([5, 7, 9])

print(X)
print(Y)
print("交集", X & Y)
print("聯集", X | Y)
A = X & Y
print("交集", A)
A = X.intersection(Y)
print("交集A = ", A)

print("==========================")

# 夏令營程式

students = {"Peter", "Norton", "Kevin", "Mary", "John",
            "Ford", "Nelson", "Damon", "Ivan", "Tom"}

Math = {"Peter", "Kevin", "Damon"}
Physics = {"Neloson", "Damon", "Tom"}

MandP = Math | Physics
print("有 %d 人參加數學和物理夏令營 : " % len(MandP), MandP)
unAttend = students - MandP
print("沒有參加任何夏令營的有 %d 人" % len(unAttend), unAttend)

print("==========================")

A = {n for n in range(1, 100, 2)}
print(type(A))
print(A)

print("==========================")

# 方法2

A = {n for n in range(1, 100, 2) if n % 11 == 0}
print(type(A))
print(A)

print("==========================")

cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    'Bloody Mary':{'Vodka','Lemon Juice','Tomato Juice','Tabasco','little Sale'}
    }

# 列出 有Vodka的酒
print("列出有Vodka的酒 : ")
for name, formulas in cocktail.items():
    if "Vadka" in formulas:
        print(name)

# 列出有 Lemon Juice的酒
print("列出Lemon Juice的酒 : ")
for name, formulas in cocktail.items():
    if "Lemon Juice" in formulas:
        print(name)

# 列出含有Rum但沒有薑的酒
print("含有Rum但沒有薑的酒")
for name, formulas in cocktail.items():
    if "Rum" in formulas and not ("Ginger" in formulas):
        print(name)

# 列出有 Lemon Juice 但沒有 Cream 或 Tabasco 的酒
print("列出有 Lemon Juice 但沒有 Cream 或 Tabasco 的酒")
for name, formulas in cocktail.items():
    if "Lemon Juice" in formulas and not formulas & {"Cream", "Tabasco"}:
        print(name)
    