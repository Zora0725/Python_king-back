a = 3
b = 4

print(a*b)

print(a**b) #次方
print(a/b) #除法
print(a//b) #整數除法 取商數
print(a%b) #取餘數

a = 3
b = 4

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

############

print("============================")

s = True
t = False
a = False

print(s or t)
print(s and t)
print(not s)
print(not t)

print("============================")

print(s and t and a)
print(s and t or a)
print(s >= t >= a)

print("--------------------------------")

x = 1
y = 2
a = 3
b = 4

result = x > y
print(result)

print("=======================================")

print(bin(8))  #二進位
print(oct(8))  #八進位
print(hex(8))  #十六進位

print("=======================================")

a = "3.1416"
a = float(a)
print(a + 10)

print("=======================================")

a = '90'
print(int(a)+10)

print("=======================================")

a = 3.1415
print(type(a))
print(type(str(a)))

print("=======================================")

b = 3.6
print(int(b))

c = 4.6
print(int(c))
print(round(c))

print("=======================================")
      
a = -2.33
print(abs(-2.33))

a = 3
print(pow(a, 3))  # a 的三次方
print(a ** 3)   #同上 寫法不同

print("=======================================")

a = 3.141592

print(round(a, 4))    #四捨五入 #a到小數點第四位

print("=======================================")

divmod_result = divmod(10, 3)  #10/3的商及餘數

list2 = [0,1,2,3,4,5,6,7,8,9,10]
print(list2[slice(0,5)])   #取索引(index) 0 到 5 不包含5
print(list2[0:5])  #同上
print(list2[1:5:2])
print(list2[slice(1,10,2)])


print("=======================================")


print(1,2,3,4,5, sep = "/")
print(1,2,3,4,5, sep = "")


#設定結尾 預設換行符號

print(1,2,3,4,5, sep = "/" , end = "\n\n")

print("=======================================")

output_txt = "帳戶餘額\n%010.2f元"%(10000.123)
print(output_txt)


print("=======================================")


print(list("123"))
print(list([4,5,6]))

print("=======================================")

left = ( (23 / 11) + 52 ) * 0.7 + 200
right = (( 28 / 26) + 51 ) * 0.7 + 207

print(left > right)
print(left , right) 

print("=======================================")

list_1 = ["1101","1102","1210"]
list_2 = range(1, 3 + 1)   #取到3停才使用3+1 

print("=======================================")


#若範圍很大

list_id = ["1101","1102","1210"]
list_name = ["台泥","亞泥","大成"]
list_length = len(list_id)
list_num = range(1, list_length + 1 )   

print("=======================================")


#迭代作法

zip_result = zip(list_1, list_2)
print(next(zip_result))   #第一個資料

print("=======================================")


#轉換list
zip_result = zip(list_num ,list_id)
zip_list = list(zip_result)
print(zip_list[0])
  
print("==================================")

for i in range(1,31):
    print(i)
    
    list1 = ["香蕉","橘子","蘋果"]
    for s in list1:
        print(s, end = ",")
        
print("==================================")


sum = 0
n = int(input("請輸入正整數"))
for i in range(1, n+1):
    sum += i
    print("1到 %d 的整數和為 %d" % (n, sum))
    
print("==================================")


#if #elif 也是 #else 完全沒有

for i in range(1,10):
    for j in range(1,10):
        product = i * j
        print("%d * %d = %-2d " % (i , j, product) , end="")
        print()
        
        
        
print("==================================")

#for為固定次數之迴圈

for i in range(1,11):
    if(i==6):
       continue
    print(i, end=",")
    
print("==================================")

n = int(input("請輸入大樓的樓層數"))
print("本大樓具有的樓層為:")
if(n > 3):
   n += 1
   for i in range(1, n+1):
       if(i==4):
           continue
       print(i, end="")
       print()
       
print("==================================")


n = int(input("請輸入大於1的整數: "))
if(n==2):
    print("2是質數! ")
else:
    for i in range(2, n):
        if(n % i ==0):
            print("%d 不是質數!" % n)
            break
        else:
            print("%d 是質數!" % n)
    
print("==================================")

#while用於沒有固定次數之迴圈

total = n = 0
while(n < 10):
    n += 1
    total += n
print(total)   #1+2+............+10=55

print("==================================")

total = person = score = 0
while(score != -1):
    person += 1
    total += score 
    score = int(input("請輸入第 %d 位學生的成績 :" % person))
average = total / (person - 1)
print("本班總成績為 %d 分，平均成績為 %5.2f 分" % (total, average))
