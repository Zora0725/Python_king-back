# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 18:39:40 2021

@author: 202107008
"""

import os

files = ['ch14_1.py', 'ch14_2.py', 'ch14_3.py']
for file in files:
    print(os.path.join('D:\\Python\\ch14', file))
    

print("--------------------------------")

import os

# 如果檔案在目前工作目錄(資料夾)下可以省略路徑
print(os.path.getsize("D:\\Python\\ch14\\ch14_1.py"))


print("--------------------------------")

import os

print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))

print("--------------------------------")

import os

totalsizes = 0
print("列出D:\\Python\\ch14工作目錄的所有檔案")
for file in os.listdir('D:\\Python\\ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join('D:\\Python\\ch14', file))
    
print("全部檔案大小是 = ", totalsizes)

print("--------------------------------")

import glob

print("方法1:列出\\Python\\ch14工作目錄的所有檔案")
for file in glob.glob('D:\\Python\\ch14\\*.*'):
    print(file)

print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*-*'):
    print(file)
    
print("--------------------------------")

import os
import stat

fn = 'D:\\Python\\ch14\\ch14_4_1.txt'
os.chmod(fn, stat.S_IXGRP)
os.chmod(fn, stat.S_IWOTH)
print("更改成功了")

print("--------------------------------")

file = 'D://Python//ch14//ch14_15.txt'
file_obj = open(file)
data = file_obj.read()
file_obj.close()
print(data)

