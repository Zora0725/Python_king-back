# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 21:46:19 2021

@author: 202107008
"""

def modifysong(songStr):
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, "")
    return songStr

def wordCount(songCount):
    global mydict  #全域變數
    songList = songCount.split()
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd:songList.count(wd) for wd in set(songList)}
    
data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}
print("以下是將歌曲大寫字母全部換成小寫同時將標點符號用空字元取代")
song = modifysong(data.lower())
print(song)

wordCount(song)
print("以下是最後執行結果")
print(mydict)

print("=========================================")

class Score():
    def __init__(self, score):     #在初始化函數 self是必須存在的
        self.score = score
        
stu = Score(50)
print(stu.score)
stu.score = 100
print(stu.score)

print("==============================================")

#將score設為私有屬性

class Score():
    def __init__(self, score):
        self.__score = score   #宣告私有屬性 在屬性名稱前加入__兩個底線
    def getscore(self):
        print("inside the getscore")
        return self.__score
    def setscore(self, score):
        print("inside the setscore")
        self.__score = score
        
stu = Score(0)
print(stu.getscore())
stu.setscore(80)
print(stu.getscore())

print("==============================================")

# 放裝飾器的差別

class Score():
    def __init__(self, score):
        self.__score = score
    @property 
    def sc(self):
        print("inside the getscore")
        return self.__score
    
    @sc.setter
    def sc(self, score):
        print("inside the setscore")
        self.__score = score
        
stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)

print("==============================================")

class Square():
    def __init__(self, sideLen):
        self.__sideLen = sideLen
    @property 
    def area(self):
            return self.__sideLen ** 2 # **是平方的意思
obj = Square(10)
print(obj.area)

print("==============================================")

class Counter():
    counter = 0
    def __init__(self):
        Counter.counter += 1
    @classmethod
    def show_counter(cls):
        print("class method")
        print("counter = ", cls.counter)
        print("counter = ", Counter.counter)
        
one = Counter()    #建立類別物件
two = Counter()   #每次建立Counter()類別物件，類別屬性值會更新
three = Counter()
Counter.show_counter()

print("==============================================")

class Person():
    def __init__(self, name):
        self.name = name
class LawerPerson(Person):
    def __init__(self, name):
        self.name = name + "律師"
        
hung = Person("洪雨水")
lawer = LawerPerson("洪雨水")
print(hung.name)
print(lawer.name)

print("==============================================")

