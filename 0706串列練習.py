# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:27:32 2021

@author: USER
"""

#方程式求根

a = 3
b = 5
c = 1

r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f"{r1 = :6.4f} , {r2 = :6.4f}")

#########################

#潤年程式

print("判斷輸入年份是否為潤年")
year = input("請輸入年份: ")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400

if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print(f"{year}是潤年")
        
    else:
        print(f"{year}不是潤年")
        
else:
    print(f"{year}不是潤年")
    
    ###################################
    
#串列

james = [23,19,22,31,18]
print("列印james串列", james)

James = ["Lebron Jame",23, 19, 22,  31, 18]
James = ("列印james串列", james)

fruits = ["蘋果","香蕉","橘子"]
print("列印fruits串列", fruits)

cfruits = ["apple", "banana", "orange"]
print("列印cfruits的串列", cfruits)

ielts = [5.5, 6.0, 6.5]
print("列印IELTSt成績", ielts)
#列印串列資料型態
print("串列james的資料型態是", type(james))

#############################

james = [23, 19, 22, 31, 18]
game1, game2, game3, game4, game5 = james
print("列印james各場次的得分", game1, game2, game3, game4, game5)
 
######################################

#串列切片

warriors = ['curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
first3 = warriors[:3]
print("前三名球員", first3)
n_to_last = warriors[1:]
print("球員索引1到最後", n_to_last)
last3 = warriors[-3:]
print("後三名球員", last3)

#如果是-1

warriors = ['curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print("最後一名球員", warriors[-1])

james = [23, 19, 22, 31, 18]
print("最後一場得分", james[-1])
mixs = [9, 20.5, "Deepmind"]
print("最後一筆元素", mixs[-1])

#################################

james = [23, 19, 22, 31, 18]
games = len(james)
print(f"經過{games} 場比賽最高分為 = {max(james)}")
print(f"經過{games} 場比賽最低分為 = {min(james)}")
print(f"經過{games} 場比賽得分總計為 = {sum(james)}")

###############

#        0 , 1 , 2 , 3 , 4
james = [23, 19, 22, 31, 18]
print("舊的James比賽分數", james)
james[4] = 28
print("新的james比賽分數", james)

########

James = ["Leborn James", 23, 19, 22, 31, 18]
Love = ["Kevin Love", 20, 18, 30, 22, 15]
game3 = James[4] + Love[4]
LKgame = James[0] + "和" + Love[0] + "第四場總得分 = "
print(LKgame, game3)

print(type(James))

#########

cars = ["Toyota", "Nissan", "Honda"]
print(f"cars的串列長度是 = {len(cars)}")
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print(f"cars串列長度是 = {len(cars)}")
else:
    print("cars串列內沒有元素資料")
nums = []
print(f"num串列長度是 = {len(nums)}")
if len(nums):
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")
    
######################

cars = ['bmw', 'benz', 'audi']
carF = "我開的第一部車是" + cars[1].title()
carN = "我現在開的車是" + cars[0].upper()
print(carF,carN)

######################

strM = " DeepStone "
strL = strM.lstrip()   #刪除字串左邊多餘的空白
strR = strM.rstrip()   #刪除字串右邊多餘的空白
strB = strM.lstrip()   #先刪除字串左邊多餘的空白
strB = strB.rstrip()  #再刪除字串又邊多餘的空白
str0 = strM.strip()   #一次刪除頭尾的多餘空白

print("%s" % strM)
print("%s" % strL)
print("%s" % strR)
print("%s" % strB)
print("%s" % str0)

##############################

string = input("請輸入你的名字 :.")
print("/%s/" % string)
string = input("請輸入你的名字: ")
print("/%s/" % string.strip())

#############################

list = [1, 2, 3, 4, 5, 6]
list2 = list[0:2]
print(list2)

list3 = list[0:6:2]
print(list3)

list4 = list[0:3]
print(list4)

list5 = list[0:6:3]
print(list5)

#################################

cars = ["honda",'bmw','toyota','ford']
print("目前串列大小 = ",cars)
print("使用sort()由大排到小")
cars.sort(reverse=True)
print("排序串列結果 = ",cars)

nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort()排列由大到小")
nums.sort(reverse=True)
print("由大到小排列內容 = ",nums)

#######################

cars = ["honda",'bmw','toyota','ford']
print("目前排序內容 = ",cars)
print("使用sorted()來排序" , cars)
cars_sorted = sorted(cars)
print("排序串列結果 = ",cars_sorted)
print("原先串列內容", cars)

######################
"不寫了" 