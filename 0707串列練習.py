# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:38:35 2021

@author: USER
"""

mysports = ['basketball','baseball']
friendsports = mysports

print("列出MYSPORTS的位址 = " , id(mysports))
print("列出friendsport的位址 = ", id(friendsports))
print("我喜歡的運動 = " ,mysports)
print("朋友喜歡的運動 = ", friendsports)
mysports.append('football')   #新增項目
friendsports.append('soccer')  #新增項目
print("新增運動項目後")
print("列出mysports的位址 = ", id(mysports))
print("列出friendsports的位址 = ", id(friendsports))
print("列出我喜歡的最新運動 = ", mysports)
print("列出朋友喜歡的最新運動", friendsports)


mysports = ['basketball','baseball']
friendsports = mysports[:]    #切片拷貝

print("列出MYSPORTS的位址 = " , id(mysports))
print("列出friendsport的位址 = ", id(friendsports))
print("我喜歡的運動 = " ,mysports)
print("朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print("新增運動項目後")
print("列出mysports的位址 = ", id(mysports))
print("列出friendsports的位址 = ", id(friendsports))
print("列出我喜歡的最新運動 = ", mysports)
print("列出朋友喜歡的最新運動", friendsports)

#######################

print("=============================================")


a = [1, 2, 3, [4, 5, 6]]
b = a.copy()
print(id(a))
print(id(b))

a.append(7)  #增加元素
print(a,b)

##################

path = ['d','ch6','ch6_49.py']
connect = '\\'
print(connect.join(path))
connect = '*'
print(connect.join(path))

print("=============================================")


###################

msg = "CIA Mark told CIA Linda that the secret USB had given to CIA Peter"
print("字串開頭是GIA:" , msg.startswith("CIA"))  
print("字串結尾是CIA: ", msg.endswith("CIA"))   #是Peter
print("CIA出現的次數: ", msg.count("CIA")) 
msg = msg.replace("Linda","Lxx")  ###元素1被取代為元素2
print("新的msg內容: " , msg)

print("=============================================")


###################

password = "deepmind"
ch = input("請輸入字元 = ")
print("in的運算式")
if ch in password:
    print("輸入字元在密碼中!!")
else:
    print("輸入字元不在密碼中!!")
print("not in運算式")
if ch in password:
    print("輸入字元不在密碼中=ˇ=")
else:
    print("輸入字元在密碼中~~")
    
print("=============================================")

#################

fruits = ['apple', 'banana', 'watermelon']
fruit = input("請輸入水果: ")
if fruit in fruits:
    print("這個水果已經有了")
else:
    fruits.append(fruit)
    print("已加入新的水果", fruits)

print("=============================================")

######################
#位址運用#

x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y ,z ,r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))
r = x 
print(f"{x = },{y = },{z = }, {r = }")
print(f"x位址 = {id(x)}, y位址 = {id(y)}, z位址 = {id(z)}, r位址 = {id(r)}")

#########################
print("=============================================")

x = 10
y = 10
z = 15
r = z - 5
boolean_value = x is y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

boolean_value = x is not y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is not z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is not r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

print("=============================================")

mysports = ["basketball", "baseball"]
sports1 = mysports
sports2 = mysports[:]
print(f"我最喜歡的運動 = {mysports}", f"位址是 = {id(mysports)}")
print(f"運動1     = {sports1}", f"位址是 = {id(sports1)}")
print(f"運動2     = {sports2}", f"位址是 = {id(sports2)}")
 

bool_value = mysports is sports1
print("我最喜歡的運動 is 運動1  = ", bool_value)

bool_value = mysports is sports2
print("我最喜歡的運動 is 運動2  = ", bool_value)

bool_value = mysports is not sports1
print("我喜歡的運動 is not 運動1   = ", bool_value)

bool_value = mysports is not sports2
print("我最喜歡的運動 is not 運動2 = ", bool_value)

print("=============================================")

x = []
if x is None:
    print("It is None")
else:
    print("It is not None")

print("=============================================")

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)
print(enumerate_drinks)
print("下列式輸出enumerate物件類型")
print(type(enumerate_drinks))

print("=============================================")

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)
print("轉成串列輸出，初始值是 = 0 ", list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)
print("轉成串列輸出，初始索引值是10", list(enumerate_drinks))
print(type(enumerate_drinks))

print("=============================================")

