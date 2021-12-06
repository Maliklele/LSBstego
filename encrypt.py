from PIL import Image


_TEXT_PATH = "text.txt"
_IMAGE_PATH = "images\original.png"



#Reeading text file and returning array with bits of
def readFile(path):
    fileR = open("text.txt", 'r')
    msg = fileR.read()
    binaArr = []
    for element in msg:  
        binaArr.append(format(ord(element), '08b'))
    splitBinaArray = []
    #print(binaArr)
    for x in binaArr:
        splitBinaArray.append(x[0:2])
        splitBinaArray.append(x[2:4])
        splitBinaArray.append(x[4:6])
        splitBinaArray.append(x[6:8])
    
    for x in range(4):
        if (len(splitBinaArray)%3!=0):
            splitBinaArray.append('00')
        else:
            break

    return splitBinaArray


    
    

bina = readFile(_TEXT_PATH)
#print(bina)

originalImage = Image.open(_IMAGE_PATH)
processedImage = originalImage.copy()


i=0
halt=False
for x in range(processedImage.size[0]):
    for y in range(processedImage.size[1]):
        if(i<len(bina)):
            
            _rgb = processedImage.getpixel((x,y))
            _r=int(format(_rgb[0],'08b')[0:6]+bina[i],2)
            _g=int(format(_rgb[1],'08b')[0:6]+bina[i+1],2)
            _b=int(format(_rgb[2],'08b')[0:6]+bina[i+2],2)
            
            processedImage.putpixel((x,y),(_r,_g,_b))
            print(processedImage.getpixel((x,y)))
            i=i+3
        else:
            halt=True
            break
    if(halt):
        break

print("Text size = ",len(bina))

print("Image mode", processedImage.mode)
print("Image Size",processedImage.size[0],"x",processedImage.size[1],"=",processedImage.size[0]*originalImage.size[1])


print("L:",len(bina))
processedImage.save("images\processed.png",format="png",quality=100)


