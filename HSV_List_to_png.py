from PIL import Image
import sys

width = 64
height = 64

skin0  = Image.new( mode = "HSV", size = (width, height), color = (0, 0, 255) )
H=[]
S=[]
V=[]
i=0

if len(H)+len(S)+len(V)<1632*3:
    print('Either your lists are too short or you have not pasted them in yet!')
    exit(1)


for x in range(8,16):
    for y in range(8,16):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(0,8):
    for y in range(8,16):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(16,24):
    for y in range(8,16):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(8,16):
    for y in range(0,8):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(16,24):
    for y in range(0,8):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(24,32):
    for y in range(8,16):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(20,28):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(32,40):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(16,20):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(28,32):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(20,28):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(28,36):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(44,48):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(40,44):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(48,52):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(52,56):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(44,48):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(48,52):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(36,40):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(32,36):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(40,44):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(44,48):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(36,40):
    for y in range(48,52):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(40,44):
    for y in range(48,52):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(4,8):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(0,4):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(8,12):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(12,16):
    for y in range(20,32):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(4,8):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(8,12):
    for y in range(16,20):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(20,24):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(16,20):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(24,28):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(28,32):
    for y in range(52,64):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(20,24):
    for y in range(48,52):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
for x in range(24,28):
    for y in range(48,52):
        skin0.putpixel((x,y),(H[i],S[i],V[i]))
        i=i+1
skin=skin0.convert("RGB")
skin.save("Your_Skin.png", "PNG")
