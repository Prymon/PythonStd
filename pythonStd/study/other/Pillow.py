'''
Created on 2015年8月28日

@author: dimen
'''
from PIL import Image
im = Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((100,100))
im.save('thumbTest.jpg','JPEG')