# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:33:56 2021

@author: 202107008
"""

# 文件分析

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}
print("原始歌曲")
print(song)

#大寫改小寫
songLower = song.lower()
print("小寫")
print(songLower)

# 標點符號改空格

for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch, " ")
print("沒有標點符號的歌曲")
print(songLower)

# 將歌曲轉換成串列
songlist = songLower.split()
print("以下為歌曲串列")
print(songlist)

# 將歌曲串列處理成字典
for wd in songlist:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1
        
print("列印結果")
print(mydict)

print("==========================")

#星座運勢

season = {'水瓶座':'1月20日 - 2月18日, 須警惕小人',
          '雙魚座':'2月19日 - 3月20日, 凌亂中找立足',
          '白羊座':'3月21日 - 4月19日, 運勢比較低迷',
          '金牛座':'4月20日 - 5月20日, 財運較佳',
          '雙子座':'5月21日 - 6月21日, 運勢好可錦上添花',
          '巨蟹座':'6月22日 - 7月22日, 不可鬆懈大意',
          '獅子座':'7月23日 - 8月22日, 會有成就感',
          '處女座':'8月23日 - 9月22日, 會有挫折感',
          '天秤座':'9月23日 - 10月23日, 運勢給力',
          '天蠍座':'10月24日 - 11月22日, 中規中矩',
          '射手座':'11月23日 - 12月21日, 可羨煞眾人',
          '魔羯座':'12月22日 - 1月19日, 需保有謙虛',
          }

word = input("請輸入欲查詢的星座 : ")
if word in season:
    print(word, "本月運勢", season[word])
else:
    print("星座輸入錯誤")
    
print("==========================")

# 加密文件凱薩密碼

abc = "abcdefghijklmnopqrstuvwxyz"
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))
print("列印編碼字典\n", encry_dict)

msgTest = input("請輸入原始字串: ")

cipher = []
for i in msgTest:
    v = encry_dict[i]
    cipher.append(v)
ciphertext = "".join(cipher)

print("原始字串 = ", msgTest)
print("加密字串", ciphertext)
