import random, operator, math, numpy, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def ellipse(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-org.size[0], org.size[0] - 1)
    y = random.randint(-org.size[1] , org.size[1] - 1)
    w = random.randint(x + 1, org.size[0])
    h = random.randint(y + 1, org.size[1])
    col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, 255)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def darkPicture(N):
    ret = Image.new('RGBA', N.size, (255, 255, 255, 0))
    return ret

wartosc_alphy = 126
ideal = Image.open("MonaLisa.png").convert("RGBA")
dark = darkPicture(ideal)

for i in range(10):
    dark = ellipse(ideal, dark)
    dark.show()