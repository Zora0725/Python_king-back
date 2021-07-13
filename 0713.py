# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:46:45 2021

@author: 202107008
"""

sports = { "curry":["籃球", "美式足球"],
          "Dirant":["棒球"],             # 鍵:值-串列部分
          "James":["美式足球","棒球","籃球"]}
for name, favorite_sport in sports.items():   #name為鍵 favoite_sport為值 
    print("%s 喜歡的運動是: " % name)
    for sport in favorite_sport:
        print("   ", sport)

print("==================================")

survey_dict = {}
market_survey = True

while market_survey:
    name = input("\n請輸入姓名: ")
    travel_location = input("請輸入你想去的地方: ")
    
    survey_dict[name] = travel_location
    repeat = input("是否參加市場調查? (y/n) ")
    if repeat != "y":
        market_survey = False
        
print("\n\n以下為市場調查的結果")
for user, location in survey_dict.items():
    print(user, "夢幻旅遊景點: ", location)
        
print("==================================")


seq1 = ["name","city"]  #建立串列
print(type(seq1))
list_dict1 = dict.fromkeys(seq1) #將串列轉換成字典
print("字典1", list_dict1) 
list_dict2 = dict.fromkeys(seq1, "Chicago") 
print("字典2", list_dict2) 
seq2 = ("name", "city") #建立元祖
print(type(seq2)) 
tup_dict1 = dict.fromkeys(seq2) 
print("字典3", tup_dict1) 
tup_dict2 = dict.fromkeys(seq2, "New York") 
print("字典4", tup_dict2)

print("==================================")

fruits = {"apple":20, "orange":25}  #字典
ret_value1 = fruits.get("orange") #找orange<鍵>的值
print("value = ", ret_value1) 
ret_value2 = fruits.get("grape") 
print("values = ", ret_value2)  #沒有這個對應的鍵的值結果是None
ret_value3 = fruits.get("grape", 10)
print("value = ", ret_value3)

print("==================================")

# setdefault 鍵在字典內的應用

fruits = {"apple":20, "orange":25}
ret_value = fruits.setdefault("orange")  #找orange的值
print("value = ", ret_value)  #回傳值
print("fruit的字典", fruits)  
ret_value = fruits.setdefault("orange", 100)
print("fruit字典", fruits)

print("==================================")

# setdefault 鍵不在字典內的應用

person = {"name":"John"}
print("字典原先的內容", person)

# age不存在
age = person.setdefault("age")
print("增加age", person)
print("age = ", age)

# sex不存在
sex = person.setdefault("sex")
print("增加sex", person)
print("sex = ", sex)

print("==================================")

