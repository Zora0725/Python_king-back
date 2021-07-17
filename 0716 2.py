# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 21:14:27 2021

@author: 202107008
"""

def mutifunction(x1, x2):
    """加減乘除 除四則運算"""
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    diveresult = x1 / x2
    return addresult, subresult, mulresult, diveresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果", add)
print("減法結果", sub)
print("乘法結果", mul)
print("除法結果", div)

print("================================================")

def guess_info(firstname, middlename, lastname, gender):
    """整合客戶資料"""
    if gender == "M":
        welcome = lastname + middlename + firstname + "先生歡迎您"
    else:
        welcome = lastname + middlename + firstname + "小姐歡迎您"
    return welcome

info1 = guess_info("宇","果","洪","M")
info2 = guess_info("雨","冰","洪","F")
print(info1)
print(info2)

print("================================================")

def guess_info(firstname, lastname, gender, middlename = ""):
    """整合客戶資料"""
    if gender == "M":
        welcome = f"{lastname} {middlename} {firstname},先生歡迎您"
    else:
        welcome = f"{lastname} {middlename} {firstname}, 小姐歡迎您"
    return welcome

info1 = guess_info("龍", "成", "M")
info2 = guess_info("冰", "范", "F", "冰")
print(info1)
print(info2)

print("================================================")

def build_VIP(id, name):
    """建立VIP資訊"""
    vip_dict = {"VIP_ID":id, "name":name}
    return vip_dict

member = build_VIP("101", "Nelson")
print(member)

print("================================================")

def build_VIP(id, name, tel = ""):
    """建立VIP資訊"""
    vip_dict = {"VIP_ID":id, "name":name}
    if tel:
        vip_dict["Tel"] = tel
    return vip_dict

member1 = build_VIP("101", "Nelson")
member2 = build_VIP("102", "Herry", "0955223344")

print(member1)
print(member2)

print("================================================")

def build_VIP(id, name, tel = ""):
    """建立VIP資訊"""
    vip_dict = {"VIP_ID":id, "name":name}
    if tel:
        vip_dict["tel"] = tel
    return vip_dict

while True:
    print("建立VIP資訊系統")
    name = input("請輸入姓名 : ")
    idnum = input("請輸入VIP ID : ")
    tel = input("請輸入電話號碼 : ")
    member = build_VIP(name, idnum, tel)
    print(member, "\n")
    repeat = input("是否繼續輸入(Y/N)? 輸入非y字元可結束系統")
    if repeat != "y":
        break
    
print("歡迎下次再使用")

print("================================================")

def product_msg(customers):
    str1 = "親愛的"
    str2 = "本公司將在2021/09/01舉行產品發表會"
    str3 = "蘋果公司敬上"
    for customer in customers:
        msg = str1 + customer + "\n" + str2 + "\n" + str3
        print(msg, "\n")
        
members = ["Damon", "Peter", "Mary"]
product_msg(members)

print("================================================")

def mydate(n):
    print("副程式id(n) : ", id(n), "\t", n)  # 串列變數會改變程式內容
    n = 5
    print("副程式 id(n) = : ", id(n), "\t", n)
    
x = 1
print("主程式 id(x) : ", id(x), "\t", x)  # 一般整數變數不會改變程式內容  
mydate(x)
print("主程式 id((x) : ", id(x), "\t", x)

print("================================================")

def kitchen(unserved, served):
    """未處理的餐點轉為已服務"""
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop()
        print("菜單", current_meal)
        served.append(current_meal)
        
def show_unserved_meal(unserved):
    """顯示尚未服務的餐點"""
    print("====尚未服務的餐點====")
    if not unserved:
        print("*****沒有餐點*****", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
    
        
def show_served_meal(served):
    """顯示已服務的餐點"""
    print("========下列是已服務的餐點=======")
    if not served:
        print("沒有餐點", "\n")
    for served_meal in served:
        print(served_meal)
        
unserved = ["大麥克", "勁辣雞腿堡", "麥克雞塊"]
served = []

show_unserved_meal(unserved)
show_served_meal(served)

kitchen(unserved, served)
print("\n", "餐點處理結束", "\n")

show_unserved_meal(unserved)
show_served_meal(served)

print("================================================")

def insertChar(letter, mylist=[], inlist=[1, 2]):
    mylist.append(letter)
    inlist.append(letter)
    print(mylist)
    print(inlist)
    
insertChar("x")
insertChar("y")

print("================================================")

