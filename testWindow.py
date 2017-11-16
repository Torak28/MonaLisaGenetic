import random, operator, math, numpy, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def ellipse(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(0, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(y + 1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, 255)
    ret.ellipse(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N

def square(org, N):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(0, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(y + 1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    R = col[0]
    G = col[1]
    B = col[2]
    # eksperymentalne wydanie
    A = random.randint(0, wartosc_alphy)
    ret.rectangle(((x,y),(w,h)), fill=(R,G,B,A))
    N.paste(tmp,mask=tmp)
    return N


def find_median_colorS(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.rectangle(((x, y), (w, h)), outline= 1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median


def darkPicture(N):
    ret = Image.new('RGBA', N.size, (255, 255, 255, 0))
    return ret

wartosc_alphy = 126
ideal = Image.open("MonaLisa.png").convert("RGBA")
dark = darkPicture(ideal)

for i in range(40):
    dark = square(ideal, dark)

dark.show()