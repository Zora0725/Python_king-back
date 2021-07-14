# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:09:03 2021

@author: 202107008
"""

empty_dict = {}
print("列印類別 = ", type(empty_dict))
empty_set = set()
print("列印類別 = ", type(empty_set))

print("=======================")

fruits1 = ["apple", "orange", "apple", "banana", "orange"]
x = set(fruits1)

fruits2 = list(x)
print("列印原先串列資料", fruits1)
print("列印新的串列資料", fruits2)

print("=======================")


# 交集

math = {"kevin", "peter", "eric"}
phy = {"peter", "nelson", "tom"}
both1 = math & phy  #第一種寫法
print("兩者皆想參加", both1)
both2 = math.intersection(phy)  #第二種寫法 
print("兩者皆想參加", both2)

print("=======================")

# 聯集

math = {"kevin", "peter", "eric"}
phy = {"peter", "nelson", "tom"}
allmember1 = math | phy   #第一種寫法
print("列印出參加數學或物理夏令營的成員", allmember1)
allmember2 = math.union(phy)   #第二種寫法
print("參加數學或物理夏令營的成員", allmember2)

print("=======================")

# 差集

math = {"Kevin", "Peter", "Eric"}
physics = {"Peter", "Nelson", "Tom"}
math_only1 = math - physics  #第一種寫法
print("列出參加數學夏令營卻沒參加物理夏令營的成員", math_only1)
math_only2 = math.difference(physics)  #第二種寫法
print("參加數學夏令營沒參加物理夏令營的同學", math_only2)
physics_only1 = physics - math  #第一種寫法
print("參加物理夏令營同時沒參加數學夏令營的同學", physics_only1)
physics_only2 = physics.difference(math)   #第二種寫法
print("參加物理夏令營沒參加數學夏令營的同學", physics_only2)

print("=======================")

# 對稱差集 

math = {"Kevin", "Peter", "Eric"}
physics = {"Peter", "Nelson", "Tom"}
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員", math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員", math_sydi_physics2)

print("=======================")

# 等於

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {1, 2, 3, 4, 5}

#列出A與B集合是否相等
print("A和B集合是否相等", A == B)
#列出A與C集合是否相等
print("A和C集合是否相等", A == C)

print("=======================")

# 不相等

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {1, 2, 3, 4, 5}

#列出A和B集合是否相等
print("A和B集合是否相等", A != B)
#列出A和C集合是否相等
print("A和C集合是否相等", A != C)

print("=======================")

# in的用法

fruits = set("orange")
print("字元a是否屬於fruits集合?", "a" in "orange")
print("字元d是屬於fruits集合?", "d" in "orange")
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

