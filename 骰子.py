# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:18:34 2021

@author: USER
"""

import random

while True:
    inkey = input("按任意鍵在按[ENTER]擲骰子，直接按[ENTER]鍵結束." )
    if len(inkey) > 0:
        num = random.randint(1,6)
        print("你的骰子點數為:" + str(num))
    else:
        print("遊戲結束")
        break
    
######################################
    

import random 
print(random.sample("abcdefghijklm",3))
print(random.sample([1,2,3,4,5,6,7,8],3))
