# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:37:50 2021

@author: 202107008
"""

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in players.values():
    print(team)
    
print("================================")

noodles = {"牛肉麵":100, "肉絲麵":80, "陽春麵":60,
           "大滷麵":90, "麻醬麵":70 }
print(noodles)

#                     舊的值                      
noodlesList = sorted(noodles.items(), key = lambda item:item[1])
# 排序 從noodles取出值, 把鍵預設成匿名變數取出
print(noodlesList)
print(max(noodles.values()))   #最貴
print(min(noodles.values()))   #最便宜


print("================================")

soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}     # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]                  # 小兵組成串列
for army in armys:                                      # 列印小兵
    print(army)

print("================================")

# 建立大型字典

armys = []
for solider_number in range(50):
    solider = {"tag":"red", "score":3, "speed":"slow"}
    armys.append(solider)

for solider in armys[:3]:
    print(solider)

print(len(armys))

print("================================")

armys = []
for solider_number in range(50):
    solider = {"tag":"red", "score":3, "speed":"slow"}
    armys.append(solider)
    
print("前三名士兵的資料")
for soilder in armys[:3]:
    print(solider)

# 更改為36~38號的士兵
for solider in armys[35:38]:
    if solider["tag"] == "red":
        solider["tag"] == "blue"
        solider["score"] = 5
        solider["speed"] = "medium"

# 輸出35到40號的士兵
print("輸出35~40的士兵")
for solider in armys[34:40]:
    print(solider)

