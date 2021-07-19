# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 20:08:45 2021

@author: 202107008
"""

class Grandfather():
    """定義祖父的資產"""
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
            print("Grandfather's information")
            
class Father(Grandfather):
    """定義父親的資產"""
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()    #將祖父類別的屬性複製
    def get_info2(self):
        print("Father's information")
        
class Ivan(Father):
    """定義Ivan的資產"""
    def __init__(self):   #初始化
        self.ivanmoney = 3000   #兒子的資產資訊
        super().__init__()   #將父親的類別屬性複製
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):
        print("\nIvan的資產: ", self.ivanmoney,
              "\n父親的資產: ", self.fathermoney,
              "\n祖父的資產: ", self.grandfathermoney)
        
ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()