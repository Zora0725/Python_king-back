# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:30:28 2021

@author: 202107008
"""

def greeting():
    """我的第一個python函數設計"""
    print("python歡迎你")
    print("祝學習順利")
    print("謝謝")
    
    
# 以下程式也可稱主程式

greeting()
greeting()
greeting()
greeting()

print("=============================")

# 傳遞一個參數

def greeting(name):
    """python函數需傳遞名字"""
    print("Hi", name, "Good morning!")
greeting("Nelson")

print("=============================")

def subtract(x1, x2):
    """減法設計"""
    result = x1 - x2
    print(result)
    
print("本程式會執行a - b的運算")
a = eval(input("a = "))
b = eval(input("b = "))
print("a - b = ", end = " ")
subtract(a, b)

print("=============================")

def interest(interest_type, subject):
    """顯示興趣和主題"""
    print("我的興趣是", interest_type)
    print("在", interest_type , "中, 最喜歡的是", subject)
    print()
    
interest("旅遊", "日本")
interest("程式設計", "python")

print("=============================")

def interest(interest_type, subject):
    """顯示興趣和主題"""
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type} 中, 最喜歡的是 {subject}")
    print()
    
interest(interest_type = "旅遊", subject = "日本" )
interest(subject = "日本", interest_type = "旅遊" )

print("=============================")

def interest(interest_type, subject = "日本"):
    """顯示興趣和主題"""
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type}中, 我最喜歡的是 {subject}")
    print()
    
interest("旅遊")  #傳遞一個參數
print("=============================")

interest(interest_type = "旅遊")  #傳遞一個參數
print("=============================")

interest("旅遊", "張家界")  #傳遞兩個參數
print("=============================")

interest(interest_type = "旅遊", subject = "張家界")  #傳遞兩個參數
print("=============================")

interest(subject = "張家界", interest_type = "旅遊") #傳遞兩個參數
print("=============================")

interest("閱讀", "旅遊類") # 傳遞兩個參數 不同主題

print("=============================")

def greeting(name):
    """python函數需傳遞名字name"""
    print("Hi", name, "Good Morning")
ret_value = greeting("Nelson")
print(f"greeting()的傳回值 = {ret_value}")
print(f"{ret_value}, 的 type = {type(ret_value)}")

print("=============================")

val = None
if val:
    print("I love JAVA")
else:
    print("I LOVE PYTHON")
    
print("=============================")

def is_None(string, x):
    if x is None:
        print(f"{string} = None")
    elif x:
        print(f"{string} = True")
    else:
        print(f"{string} = False")
    
is_None("空串列", [])
is_None("空元組", ())
is_None("空字典", {})
is_None("空集合", set())
is_None("None", None)
is_None("True", True)
is_None("False", False)

print("=============================")

def subtract(x1, x2):
    """減法設計"""
    result = x1 - x2
    return result
print("本程式會執行a - b 的運算")
a = int(input("a = "))
b = int(input("b = "))
print("a - b = ", subtract(a, b))

print("=============================")

def subtract(x1, x2):
    """減法設計"""
    return x1 - x2
def addition(x1, x2):
    """加法設計"""
    return x1 + x2

print("請輸入運算")
print("1:加法")
print("2:減法")
op = int(input("輸入1/2: "))
a = int(input("a = "))
b = int(input("b = "))

if op == 1:
    print("a + b = ", addition(a, b))
elif op == 2:
    print("a - b = ", subtract(a, b))
else:
    print("運算方式有錯誤")
    
