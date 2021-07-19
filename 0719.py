# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:50:03 2021

@author: 202107008
"""

class Person():
    def job(self):
        print("我是老師")
        
class LawerPerson(Person):
    def job(self):
        print("我是律師")
        
hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()


print("=============================")

class Animals():
    """Animals類別，這是基底類別"""
    def __init__(self, animal_name, animal_age):  # 有兩個參數，初始化
        self.name = animal_name     # 定義動物的名字
        self.age = animal_age       # 定義動物的年紀
        
    def run(self):    #輸出is running
        print(self.name.title(), "is running")
        
class Dogs(Animals):    # 衍生類別
    """Dongs的類別，這是衍生類別"""
    def __init__(self, dog_name, dog_age):  # 初始化
        super().__init__("My pet " + dog_name.title(), dog_age)
        
mycat = Animals("Lucy", 5)  # 套用Animals基底類別
print(mycat.name.title(), "is", mycat.age, "years old")
mycat.run()

mydog = Dogs("Lily", 6)
print(mydog.name.title())
mydog.run()

print("=============================")

class Animals():
    """Animals類別，這是基底類別"""
    def __init__(self, animal_name, animal_age):  # 有兩個參數，初始化
        self.name = animal_name     # 定義動物的名字
        self.age = animal_age       # 定義動物的年紀
        
    def run(self):    #輸出is running
        print(self.name.title(), "is running")
        
class Dogs(Animals):    # 衍生類別
    """Dongs的類別，這是衍生類別"""
    def __init__(self, dog_name, dog_age):  # 初始化
        super().__init__("My pet " + dog_name.title(), dog_age)
        
    def sleeping(self):
        print("My Pet ", "is sleeping")
        
mycat = Animals("Lucy", 5)  # 套用Animals基底類別
print(mycat.name.title(), "is", mycat.age, "years old")
mycat.run()

mydog = Dogs("Lily", 6)
print(mydog.name.title(), "is", mydog.age, "years old.")
mydog.run()
mydog.sleeping()


print("=============================")

#兄弟類別

class Father():
    """定義父親的資產"""
    def __init__(self):
        self.fathermoney = 10000
class Ira(Father):
    """定義Ira的資產"""
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
        
class Ivan(Father):
    """定義Ivan的資產"""
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
        
    def get_money(self):
        print("Ivan的資產", self.ivanmoney,
              "\n父親的資產", self.fathermoney,
              "\nIra的資產", Ira().iramoney)  #這裡並非self.iramoney
ivan = Ivan()
ivan.get_money()

print("=============================")

        