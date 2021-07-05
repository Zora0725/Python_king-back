x = 9 // 5
print(x)

y = 9 % 5
print(y)

z = divmod(9, 5)
print(z)

x, y = z 
print(x)
print(y) 

money = 50000 * (1 + 0.015) ** 5
print("本金和是")
print(money)


car = 100000 * (1 - 0.15) ** 3
print("車子的殘值是")
print(car)

PI = 3.14159
r = 5
print("圓面積:單位是平方公分")
area = PI * r * r
print(area)

circumference = 2 * PI * r
print("圓周長:單位是公分")
print(circumference)

x = 10
y = x / 3
print(x)
print(type(x))
print(y)
print(type(y))

x = 0b1101
print(x)
y = 13
print(bin(y))

x = 0o57
print(x)
y = 47
print(oct(y))

x = 10.5
print(x)
print(type(x))
y = int(x) + 5
print(y)
print(type(y))

x = 10
print(x)
print(type(x))
y = float(x) + 10
print(y)
print(type(y))

x = -10
print("以下輸出abs()函數的應用")
print(x)
print(abs(x))

x = 5
y = 3
print("以下輸出pow()函數的應用")
print(pow(x, y))

x = 47
print("以下輸出round()函數的應用")
print(x)
print(round(x))

x = True
print(x)
print(type(x))

y = False
print(y)
print(type(y))

x = True
print(int(x))
print(type(x))

y = False
print(int(y))
print(type(y))

xt = True
x = 1 + xt
print(x)
print(type(x))

yt = False
y = 1 + yt
print(y)
print(type(y))


num1 = 222
num2 = 333

num3 = num1 + num2
print("以下數值相加")
print(num3)

numstr1 = "222"
numstr2 = "333"
numstr3 = numstr1 + numstr2
print("以下是由數值組成的字串相加")
print(numstr3)

numstr4 = numstr1 + " " + numstr2
print("以下由數值相加，同時中間再加一個空格")
print(numstr4)

str1 = "Deepmind "
str2 = "Deepen_your_mind"
str3 = str1 + str2
print("以下是一般字串相加")
print(str3)

#以下輸出使用單引號設定的字串，需使用\'
str1 = 'I can\'t stop loving  you.'
print(str1)

#以下輸出使用雙引號設定的字串，不需要使用\' 
str2 = "I can't stop loving you."
print(str2)

#以下輸出有\t跟\n字元

str3 = "I can\'t stop \nloveing you."
print(str3)

str1 = '''Silicon Stone Education is an unbiased organization concentrated on bridging the gap...'''
print(str1)  #字串內有分行符號

str2 = '''Silicon Stone Education is an unbiased organization \ concentrated on bridging the gap...'''
print(str2) #字串內沒有分行符號

str3 = "Silicon Stone Education is an unbiased organization " \
    "concentrated on bridging the gap..."
print(str3) #使用\符號

str4 = ("Silicon Stone Education is an unbiased organization " "concentrated on bridging the gap..")
print(str4) #使用小括號

str1 = "洪錦魁著作"
str2 = "PYTHON王者歸來"
str3 = "受歡迎好書"
str4 = str1 + "\n" + str2 + "\n" + str3
print(str4)

str1 = "hello!\npython!"
print("不含R字元的輸出")
print(str1)

str2 = r"hello!\npython!"
print("含R字元的輸出")
print(str2)

x = 97
print(chr(x))

x1 = 97
x2 = chr(x1)
print(x2)

x3 = ord(x2)
print(x3)

x4 = "魁"
print(hex(ord(x4)))

x5 = "賢"
print(hex(ord(x5)))

x6 = "林"
print(hex(ord(x6)))

x7 = "靖"
print(hex(ord(x7)))

