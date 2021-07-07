# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:46:29 2021

@author: USER
"""

# 使用者帳號管理系統

accounts = []
account = (input("請輸入新帳號: "))
accounts.append(account)

print("美女公司系統")
ac = (input("請輸入新帳號: "))
if ac in accounts:
    print("歡迎進入美女公司系統")
else:
    print("帳號錯誤，無法進入")

print("====================================")

# 凱薩密碼

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
print(subText)
