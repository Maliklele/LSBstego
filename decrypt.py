from PIL import Image



img = Image.open("images/processed.png")
print("Image mode", img.mode)
print("Image Size",img.size[0],"x",img.size[1],"=",img.size[0]*img.size[1])


#creating array that holds the hidden bits
bina = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        _rgb = img.getpixel((x,y))
        _r_bina = format(_rgb[0],'08b')[6:8]
        _g_bina = format(_rgb[1],'08b')[6:8]
        _b_bina = format(_rgb[2],'08b')[6:8]
        bina.append(_r_bina)
        bina.append(_g_bina)
        bina.append(_b_bina)

for x in range(3):
    if(len(bina)%4!=0):
        bina.append('00')
    else:
        break

#print(bina)
characters = []


def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new
      


x=0
while(x<len(bina)):
    if(int(bina[x]+bina[x+1]+bina[x+2]+bina[x+3],2)>127):
        break
    #print(bina[x]+bina[x+1]+bina[x+2]+bina[x+3])
    characters.append(chr(int(bina[x]+bina[x+1]+bina[x+2]+bina[x+3],2)))
    x=x+4

text = convert(characters)
print(text)
with open("decrypted.txt", "w") as f:
    f.writelines(str(text))