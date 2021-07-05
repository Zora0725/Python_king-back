# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:44:24 2021

@author: USER
"""

#地球到月球所需時間

dist = 384400
speed = 1225 
total_hours = dist // speed
days = total_hours // 24
hours = total_hours % 24
print("總共需要的天數")
print(days)
print("小時數")
print(hours)

########################    

#divmod()應用

dist = 384400
speed = 1225
total_hours = dist // speed
days, hours = divmod(total_hours, 24)
print("總共需要的天數")
print(days)
print("小時數")
print(hours)

###########################

#座標軸兩點之距離應用

x1 = 1
y1 = 8
x2 = 3
y2 = 10

dist = ((x1-x2)**2 + (y1-y2)**2) **0.5
print("兩點的距離是")
print(dist)

##############################

#print基本語法練習

num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加", num3)
str1 = str(num1) + str(num2)
print("強制轉換為字串相加", str1, sep=" $$$ ")

################################

num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加", num3, end="\t") #以TAB鍵位置分隔兩筆資料輸出
str1 = str(num1) + str(num2)
print("強制轉換為字串相加", str1, sep=" $$$$ ")

#################################

# %格式化字串使用print()輸出

"%s" % "洪錦魁"
"%d" % 90
print("%s 你的月考成績為 %d" % ("洪錦魁", 90))

score = 90
name = "洪錦魁"
count = 1
print("%s 你的第 %d 次的物理成績為 %d" % (name,count, score))

#  formatstr

score = 90
name = "洪錦魁"
count = 1
formatstr = "%s 你的第 %d 次物理成績為 %d"
print(formatstr % (name, count, score))

########################

# 格式化16進位 和 8進位輸出應用

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x,x))

# ################

x = 10
print("將整數%d \n浮點數 %f \n字串%s" % (x, x, x))
y = 9.9
print("整數%d \n浮點數%f \n字串%s" % (y, y, y))

####################

x = 100
print("x=/%6d/" %x)
y = 10.5
print("y=/%6.2f/" % y)
s = "deep"
print("s=/%6s/" % s)
print("以下是保留格數空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)


#### 靠左對齊實例

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "deep"
print("s=/%-6s" % s)

############## 正值資料

x = 10
print("x=/%+6d/" % x)
y = 10.5
print("y=/%+6.2f/" % y)

################ 成績輸出應用

print("姓名    國文    英文    總分")
print("%3s  %4d  %4d  %4d" % ("洪一號", 90, 98, 188))
print("%3s  %4d   %4d   %4d" % ("洪二號", 96, 95, 191))
print("%3s   %4d   %4d   %4d" % ("紅三號", 92, 88, 180))
print("%3s  %4d  %4d   %4d" % ("洪四號", 93, 97, 190))

#####################

x = 12345678
print("/%10.1e/" % x)
print("/%10.2E" % x)
print("/%-10.2E/" % x)
print("/%+10.2E/" % x)

#######################

score = 90
name = "洪錦魁"
count = 1
print("{} 你的第{} 次 物理成績是 {}".format(name, count, score))

#######################

score = 90
name = "洪錦魁"
count = 1
print("{0}你的第{1}次物理成績是 {2}".format(name, count, score))

#######################


#以format實作網路爬蟲

url = "http://maps.apis.com/json?city="
city = "tapei"
r = 1000
type = "scool"
print(url + city + "&radius" + str(r) + "&type" + type)
print(url  + "{}&radius={}&type={}".format(city, r, type))


#######################

name = input("請輸入姓名:")
engh = input("請輸入成績:")
print("name資料類型是{type(name)}")
print("engh資料類型是{type(engh)}")

#########################

print("歡迎使用成績輸入系統")
name = input("請輸入你的名字")
engh = input("請輸入英文成績")
math = input("請輸入數學成績")
total = int(engh) + int(math)
print(f"{name} 你的總分是{total}")

#########################

numberStr = input("請輸入數值公式") 
number = eval(numberStr)
print(f"計算結果:{number:5.2f}")

############################

print("請輸入成績輸入系統")
name = input("請輸入姓名")
engh = eval(input("請輸入英文成績"))
math = eval(input("請輸入數學成績"))
total = engh + math
print(f"{name} 你的總分是 {total}")


#################################

n1, n2, n3 = eval(input("請輸入三個數字"))
average = (n1 + n2 + n3) / 3
print(f"三個數字平均是 {average:6.2f}")

##################################

loan = eval(input("請輸入貸款金額"))
year = eval(input("請輸入貸款年限"))
rate = eval(input("請輸入年利率"))
monthrate = rate / (12*100) #改成百分比以及月利率

#計算每個月還款金額
molecules = loan * monthrate 
denominator = 1  - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator #每月還款金額
totalPay = monthlyPay * year * 12 #總共還款金額

print(f"每月還款金額 {int(monthlyPay)}")
print(f"總共還款金額 {int(totalPay)}")

#############################

#數學模組練習
import math

s = eval(input("請輸入正五角形邊長: "))
area = (5 * s **2) / (4 * math.tan(math.pi / 5))
print(f"{area = :6.2f}")

##############################

math.radians(50)

###############################

#計算經緯度距離

import math
r = 6371 #地球的半徑
x1 , y1 = 22.2838, 114.1731 #香港紅勘車站的經緯度 #第一個參數是緯度 #第二個是經度
x2 , y2 = 25.042, 121.5168 #台北車站的經緯度

d = 6371 * math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                     math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                     math.cos(math.radians(y1-y2)))

print(f"distance = {d:6.1f}")

########################
#高斯數學

starting = 1
ending = 100
d = 1

sum = int((starting + ending) * (ending - starting + 1)/2)
print(f"1到100的總和是 {sum}")
