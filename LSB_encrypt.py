from PIL import Image


_TEXT_PATH = "Input.txt"
_IMAGE_PATH = "images\original.png"
_SAVE_PATH = "images\processed.png"



#Reeading text file and returning array with bits of
def readFile(path):
    fileR = open(path, 'r')
    msg = fileR.read()
    binaArr = []
    for element in msg:  
        binaArr.append(format(ord(element), '08b'))
    splitBinaArray = []
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

originalImage = Image.open(_IMAGE_PATH)
processedImage = originalImage.copy()

imgMode = processedImage.mode
pixelNeeded = int(len(bina)/3)
pixelAvailable = processedImage.size[0]*originalImage.size[1]

print("Image mode", imgMode)
print("Pixles Needed = ",pixelNeeded)
print("Pixles Avilable",pixelAvailable)


#Stop the application if the picture is smaller than text
#   1 CHAR = 4 RGB
#   3 RGB  = 1 PIXEL
#   NEW LINE = 2 CHAR = 8 RGB
if(pixelNeeded>pixelAvailable):
    print("FAILED TO INCODE: TEXT TOO LARGE FOR THE IMAGE")
    exit(1)



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
            #print(processedImage.getpixel((x,y)))
            i=i+3
        else:
            halt=True
            break
    if(halt):
        break





processedImage.save(_SAVE_PATH,format="png",quality=100)
print("ENCODED IN IMAGE => ",_SAVE_PATH)

