# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 20:19:30 2021

@author: 202107008
"""

file = "D:/Python/ch14/sse.txt"
chunk = 100
msg = ""
with open(file) as file_obj:
    while True:
        txt = file_obj.read(chunk)
        if not txt:
            break
        msg += txt
print(msg)

print("-------------------------")

fn = "D:\Python\ch14\out14_24.txt"
string = "I love python"

with open(fn, 'w') as file_obj:    # 寫入檔案 w 
    print(file_obj.write(string))  # 傳回檔案長度
    
print("-------------------------")

fn = 'D:/Python/ch14/out14_26.txt'
x = 100

with open(fn, 'w') as file_obj:
    file_obj.write(str(x))
    
print("-------------------------")

fn = 'D:/python/ch14/out14_28.txt'
str1 = 'I love python'
str2 = 'Learn python from the best book'

with open(fn, 'w') as file_obj:
    file_obj.write(str1+"/n")
    file_obj.write(str2)
    
print("-------------------------")

src = 'D:/Python/ch14/hung.jpg'
dst = 'D:/Python/ch14/hung1.jpg'
tmp = ''

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)
        
# 開啟二進位檔案使用 rb
# 寫入二進位檔案使用 wb

