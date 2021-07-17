# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:22:02 2021

@author: 202107008
"""

def  make_icecream(*toppings):
    """列出冰淇淋的配料"""
    print("這個冰淇淋的配料如下")
    for topping in toppings:
        print("----", topping)
    print(type(toppings))
    print(toppings)
    
make_icecream("草莓醬")
make_icecream("草莓醬", "葡萄乾", "巧克力醬料")

print("=========================================")

def build_dict(name, age, **players):
    """建立球員的字典資料"""
    info = {}
    info["name"] = name
    info["age"] = age
    for key, value in players.items():
        info[key] = value
    return info

player_dict = build_dict("James", 32, City = "cleveland", State = "Ohio")
print(player_dict)

print("=========================================")

def total(data):
    return sum(data)

x = (1, 5, 10)
mylist = [min, max, sum, total]
for f in mylist:
    print(f, f(x))
    
print("=========================================")


def add(x, y):
    return x + y

def mul(x, y):
    return x*y

def running(func, arg1, arg2):
    return func(arg1, arg2)

# 主程式
result1 = running(add, 5, 10)
print(result1)
result2 = running(mul, 5, 10)
print(result2)

print("=========================================")

# 遞迴式

def factorial(n):
    """計算n的階乘, n必須是正整數"""
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
    
value = 3
print(f"{value} 的階乘結果是 = {factorial(value)}")
value = 5
print(f"{value} 的階乘結果是 {factorial(value)}")

print("=========================================")

# 全域變數

def printmsg():
    """函數本身沒有定義變數,只有執行列印全域變數功能"""
    print("函數列印", msg)
msg = "Global Variable" 
print("主程式列印", msg)
printmsg()

print("=========================================")

# nonlocal

def local_fun():
    var_nonlocal = 22
    def local_inner():
        global var_global #最上層變數
        nonlocal var_nonlocal  #上一層變數
        var_global = 111
        var_nonlocal = 222
    local_inner()
    print("local_fun輸出 var_global = ", var_global)
    print("locat_fun輸出 var_nonlocat = ", var_nonlocal)

var_global = 1
var_nonlocal = 2
print("主程式輸出 var_gloval = ", var_global)
print("主程式輸出 var_nonlocal = ", var_nonlocal)

var_global = 1
var_nonlocal = 2
print("主程式輸出 var_global = ", var_global)
print("主程式輸出 var_nonlocal = ", var_nonlocal)
local_fun()
print("主程式輸出 var_global = ", var_global)
print("主程式輸出 var_nonlocal = ", var_nonlocal)

print("=========================================")

def myRange(start = 0, stop = 100, step = 1):
    n = start
    while n > stop:
        yield n
        n += step

print(type(myRange))
for x in myRange(0, 5):
    print(x)
    
print("=========================================")

def upper(func):     #裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        
        print("函數名稱 :", func.__name__)
        print("函數參數 :", args)
        return newresult
    return newFunc

def greeting(string):    #問候函數
    return string

mygreeting = upper(greeting)  # 手動裝飾器
print(mygreeting("Hello, python!"))

print("=========================================")

def errcheck(func):
    def newFunc(*args):
        if args[1] != 0:
            result = func(*args)  # args是任意數量的字典
        else:
            result = "除數不可為0"
        print("函數名稱: ", func.__name__)
        print("函數參數: ", args)
        print("執行結果 :", result)
    return newFunc

@errcheck
def mydiv(x, y):
    return x/y

print(mydiv(6, 2))
print(mydiv(6, 0))

print("=========================================")


# 就算是無謂的練習也好
# 起碼我做了對吧