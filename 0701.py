# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:18:35 2021

@author: USER
"""

print("===========================================================")

#######################################################################

score = []
total = inscore = 0
while(inscore != -1):
    inscore = int(input("請輸入學生的成績: "))
    score.append(inscore)
print("共有 %d 的學生" %(len(score) - 1))
for i in range(0, len(score) -1 ):
    total += score[i]
average = total / (len(score) -1)
print("本班總成績為 %d 分，平均成績為: %5.2f 分" % (total, average))
#######################################################################

L = [1,2,3,4,5]

del L[1:3]
print(L)

########################################################################

tuple4 = (1,2,3,4)
n = len(tuple4)
print(tuple4)

##########################################################################

