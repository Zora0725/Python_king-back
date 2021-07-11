# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:33:21 2021

@author: 202107008
"""

# 購物車設計

store = "ABC購物中心"
products = ['電視', '冰箱', '洗衣機', '電扇', '冷氣']
cart = []
print(store)
print(products, "\n")

while True:
    msg = input("請輸入今日購買商品(q = quit)")
    if msg == 'q' or msg == 'Q':
        break
    else:
        if msg in products:
            cart.append(msg)
print("今日購買的商品", cart)

print("========================================")

# 成績系統進階

score = [[1, '陳曉明', 80, 95, 88, 0, 0, 0], [2, '王大川', 98, 97, 96, 0, 0, 0],
         [3, '吳大山', 91, 93, 95, 0, 0, 0],[4, '洪冰興', 92, 94, 90, 0, 0, 0],
         [5, '陳仙女', 92, 97, 80, 0, 0, 0]]
print("填入總分與成績")
for i in range(len(score)):
    score[i][5] = sum(score[i][2:5])
    score[i][6] = round((score[i][5] / 3), 1)
    print(score[i])
    score.sort(key=lambda x:x[5], reverse=True)

print("填入名次")
for i in range(len(score)):
    score[i][7] = i + 1
    print(score[i])

score.sort(key = lambda x:x[0])
print("最後成績單")
for i in range(len(score)):
    print(score[i])

print("========================================")


