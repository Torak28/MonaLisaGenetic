import random, operator, math, numpy, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def crop4(org):
    ret = []
    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.append(org.crop(leftT))
    ret.append(org.crop(rightT))
    ret.append(org.crop(leftB))
    ret.append(org.crop(rightB))

    return ret

def assemble4(org, tab):
    ret = Image.new('RGBA', org.size)

    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.paste(tab[0], leftT)
    ret.paste(tab[1], rightT)
    ret.paste(tab[2], leftB)
    ret.paste(tab[3], rightB)

    return ret

def assemble16(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble4(org1[0], [tab[0], tab[1], tab[2], tab[3]]))
    pic.append(assemble4(org1[1], [tab[4], tab[5], tab[6], tab[7]]))
    pic.append(assemble4(org1[2], [tab[8], tab[9], tab[10], tab[11]]))
    pic.append(assemble4(org1[3], [tab[12], tab[13], tab[14], tab[15]]))

    ret = assemble4(org, pic)

    return ret

a1 = Image.open('E:\INZ\INZ8v5\m1\m1-499.png').convert("RGBA")
a2 = Image.open('E:\INZ\INZ8v5\m2\m2-499.png').convert("RGBA")
a3 = Image.open('E:\INZ\INZ8v5\m3\m3-499.png').convert("RGBA")
a4 = Image.open('E:\INZ\INZ8v5\m4\m4-499.png').convert("RGBA")
a5 = Image.open('E:\INZ\INZ8v5\m5\m5-499.png').convert("RGBA")
a6 = Image.open('E:\INZ\INZ8v5\m6\m6-499.png').convert("RGBA")
a7 = Image.open('E:\INZ\INZ8v5\m7\m7-499.png').convert("RGBA")
a8 = Image.open('E:\INZ\INZ8v5\m8\m8-499.png').convert("RGBA")
a9 = Image.open('E:\INZ\INZ8v5\m9\m9-499.png').convert("RGBA")
a10 = Image.open('E:\INZ\INZ8v5\m10\m10-499.png').convert("RGBA")
a11 = Image.open('E:\INZ\INZ8v5\m11\m11-499.png').convert("RGBA")
a12 = Image.open('E:\INZ\INZ8v5\m12\m12-499.png').convert("RGBA")
a13 = Image.open('E:\INZ\INZ8v5\m13\m13-499.png').convert("RGBA")
a14 = Image.open('E:\INZ\INZ8v5\m14\m14-499.png').convert("RGBA")
a15 = Image.open('E:\INZ\INZ8v5\m15\m15-499.png').convert("RGBA")
a16 = Image.open('E:\INZ\INZ8v5\m16\m16-499.png').convert("RGBA")

ideal = Image.open("MonaLisa.png").convert("RGBA")

ass = assemble16(ideal, [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16])
ass.show()
#ass.save(disk + "/" + folder + "/output.png")