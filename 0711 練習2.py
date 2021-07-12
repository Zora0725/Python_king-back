# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:04:32 2021

@author: 202107008
"""

fruits = ("apple", "orange")
print("原始fruits元祖元素")
for fruit in fruits:
    print(fruit)
    
fruits = ("watermelon", "grape")
print("\n新的fruits元祖元素")
for fruit in fruits:
    print(fruit)
    
print("==============================")


drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)
print("轉成元組輸出，起始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)
print("轉成元組輸出，起始值是 10 = ", tuple(enumerate_drinks))

print("==============================")

(name, (math, eng)) = ('Tom', (90, 95))
print('name = '+ name + "\n" + 'math = ' + str(math) + "\n" +'eng = ' + str(eng))

print("==============================")

fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipDate = zip(fields, info)
sold_info = list(zipDate)
for city, sales in sold_info:
    print(f"{city} 銷售金額 {sales}")    

print("==============================")

# 字典

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print(fruits)
print(noodles)

#列出字典的資料型態
print("字典fruits資料型態是", type(fruits))

