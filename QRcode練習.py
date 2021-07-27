# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:14:11 2021

@author: 202107008
"""

import qrcode

codeText = 'https://github.com/Zora0725'
img = qrcode.make(codeText)
print("檔案格式", type(img))
img.save("C:/Python/MyGitHubZora.jpg")


print("------------------------")

import qrcode
from PIL import Image

pict = Image.open("C:/Python/test1.jpg")
cropPict = pict.crop((80, 30, 150, 100))
cropPict.save("C:/Python/abcd123.jpg")

qr = qrcode.QRCode(version=5, 
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("https://github.com/Zora0725")
img = qr.make_image(fill_color="blue")
width, height = img.size
with Image.open("C:/Python/abcd123.jpg") as object:
    object_width, object_height = object.size
    img.paste(object, ((width-object_width)//2, (height-object_height)//2))
img.save("C:/Python/MyGitHubZora0725.jpg")

    