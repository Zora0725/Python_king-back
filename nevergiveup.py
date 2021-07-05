# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:50:22 2021

@author: USER
"""

def func_1(x):
    print(x +1)
    return x + 2 

y= func_1(3)  
print(y) 

#######################################################

def main(n):
    sumi = 0
    for i in range(1, n + 1):
        sumi += 1 / (2 ** i)
        
        return sumi
    
result = main(10)
print(result)

###########################################ˇ

dict1={"林小明":85,"曾山水":93,"劉美麗":67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的成績為 %d 分" % (listkey[i], listvalue[i]))


########################################

dict1={"林小明":85,"曾山水":93,"鄭美麗":67}
dict1[ "黃明品" ] = 71
dict1["陳莉莉"] = 98
listitem = dict1.items()
for name, score in listitem:
    print("%s 的成績: %d 分 " % (name, score))
    
############################################

def ctof(c):
    f = c * 1.8 + 32
    return f

input = float(input("請輸入攝氏溫度: "))
print("華氏溫度為: %5.1f 度" % ctof(input))

########################################


def GetArea(width, height):
    return width * height
area1 = GetArea(6, 9)
area2 = GetArea(width = 6, height = 9)
area3 = GetArea(width = 9 ,height = 6)
print(area1, area2, area3)


############################################

##############################

def calsum(*params):
    total = 0
    for param in params:
        total += param
    return total

print("不定數目範例: ")
print("2 個參數:calsum(4,5) = %d" % calsum(4,5))
print("3個參數: calsum(4,5,12) = %d" % calsum(4,5,12))
print("4個參數: calsum(4,5,12,8) = %d" % calsum(4,5,12,8)) 

####################################

def scope():
    var1 = 1
    return var1, var2

var1 = 10
var2 = 20
x, y = scope()
print(x, y)
print(var1, var2)


######################################

