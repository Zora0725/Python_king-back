# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:33:17 2021

@author: 202107008
"""

import os


print("檔案或資料夾存在 = ", os.path.exists('ch14'))
print("檔案或資料夾存在 = ", os.path.exists('D:\\Python\\ch14'))
print("檔案或資料夾存在 = ", os.path.exists('ch14_4.py'))
print("--------------------")

print("是絕對路徑 = ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 = ", os.path.isabs('D:\\Python\\ch14\\ch14.4_py'))
print("---------------------")

print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14\\ch14.4_py'))
print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14'))
print("------------------------")

print("是檔案 = ", os.path.isfile('D:\\Python\\ch14\\ch14.4_py'))
print("是檔案 = ", os.path.isfile('D:\\Python\\ch14'))

print("----------------------------------")

import os

mydir = 'testch14'

if os.path.exists(mydir):
    print("已經存在 %s " % mydir)
    
else:
    os.mkdir(mydir)
    print("建立 %s 資料夾成功 " % mydir)
    
print("----------------------------------")

import os

mydir = 'testch14'

if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除 %s 資料夾成功" % mydir)
    
else:
    print("刪除 %s 資料夾不存在" % mydir)
    
print("----------------------------------")

import os

myfile = 'test.py'
if os.path.exists(myfile):
    os.remove(myfile)
    print(f"刪除 {myfile} 檔案成功")
    
else:
    print(f"{mydir} 檔案不存在")
    
print("===========================")

import os

newdir = 'D:\\Python'
currentdir = os.getcwd()
print("列出目前的資料夾 ", currentdir)

# 如果newdir不存在就建立此資料夾
if os.path.exists(newdir):
    print("已經存在 %s " % newdir)
    
else:
    os.mkdir(newdir)
    print("建立 %s 資料夾成功" % newdir)

# 將目前工作資料夾改至newdir

os.chdir(newdir)
print("列出最新工作資料夾", os.getcwd())

# 將目前的工作資料夾返回

os.chdir(currentdir)
print("列出返回工作資料夾", currentdir)

    
print("===========================")


import os

print(os.path.join('D:\\', 'Python', 'ch14', 'ch14_9.py'))
print(os.path.join('D:\\Python', 'ch14', 'ch14_9.py'))
print(os.path.join('D:\\Python\\ch14', 'ch14_9.py'))

print("===========================")

