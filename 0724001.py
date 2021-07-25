# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:55:02 2021

@author: 202107008
"""

import os

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:", dirName)
    print("目前子目路名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列: ", fileNames, "\n")
    
print("-------------------------------------")

file = "D:\\Python\\ch14\\ch14_15.txt"
with open(file) as file_obj:
    for line in file_obj:
        print(line)
        
print("-------------------------------------")

file = "D:\\Python\\ch14\\ch14_15.txt"
with open(file) as file_obj:
    for line in file_obj:
        print(line.rstrip())
        
print("-------------------------------------")




    
    