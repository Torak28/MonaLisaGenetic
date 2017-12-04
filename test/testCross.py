import random, operator, math, os, time
from PIL import Image, ImageDraw, ImageChops, ImageStat

def find_median_colorS(N, x, y, w, h):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    if x < 0:
        x = 1
    if y < 0:
        y = 1

    ret.rectangle(((x, y), (w, h)), outline=1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median

def square(org, N, WA):
    tmp = Image.new('RGBA', N.size)
    ret = ImageDraw.Draw(tmp)
    x = random.randint(-20, org.size[0] - 1)
    y = random.randint(-20, org.size[1] - 1)
    if x < 0:
        w = random.randint(1, org.size[0] + 20)
    else:
        w = random.randint(x + 1, org.size[0] + 20)
    if y < 0:
        h = random.randint(1, org.size[1] + 20)
    else:
        h = random.randint(y + 1, org.size[1] + 20)
    col = find_median_colorS(org, x, y, w, h)
    R = col[0]
    G = col[1]
    B = col[2]
    A = WA
    ret.rectangle(((x, y), (w, h)), fill=(R, G, B, A))
    N.paste(tmp, mask=tmp)
    N = Image.alpha_composite(N, tmp)
    return N

def darkPicture(N):
    ret = Image.new('RGBA', N.size, (0, 0, 0, 0))
    return ret

def Add(P1, P2):
    ret = Image.alpha_composite(P1, P2)
    return ret

ideal = Image.open("test.png").convert("RGBA")
wartosc_alphy = 120

a1 = darkPicture(ideal)
a2 = darkPicture(ideal)

ass = 10
for i in range(25):
    a1 = square(ideal, a1, ass)
    a2 = square(ideal, a2, ass)
    ass = ass + 10

a1.show()
a2.show()

xd = Add(a1,a2)
xd.show()
