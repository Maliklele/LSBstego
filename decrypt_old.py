import PIL as pl
from PIL import Image
import numpy as np
import math 


#Reading text
fileR = open("text.txt", 'r')

msg = fileR.read()
msgArr = []
for element in msg:
    msgArr.append(ord(element))
print(msgArr,"len: ",len(msgArr)) 
imgSizOpt = int(math.sqrt(len(msgArr)))+1

for x in range(3):
    if(len(msgArr)%3!=0):
        msgArr.append(0)
    else:
        break


#Write to image pixels
img = Image.new("RGB",(imgSizOpt,int(imgSizOpt)),color='black')
print("Image Mode: ",img.mode)

c=0
stop=False
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if(c>=len(msgArr)):
            stop=True
            break
        else:
            img.putpixel((i, j), (msgArr[c], msgArr[c+1], msgArr[c+2]))
            c=c+3
    if(stop):
        break
img.save('pil.png')



#Read from image pixels
imgR=Image.open("pil.png")
imgMsg = []
for i in range(imgR.size[0]): # for every pixel:
    for j in range(imgR.size[1]):
        r,g,b=imgR.getpixel((i,j))
        imgMsg.append(chr(r))
        imgMsg.append(chr(g))
        imgMsg.append(chr(b))
        
print(''.join(imgMsg))





