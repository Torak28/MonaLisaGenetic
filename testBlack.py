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
    ret1 = Image.new('RGBA', org.size)
    ret2 = Image.new('RGBA', org.size)
    ret3 = Image.new('RGBA', org.size)
    ret4 = Image.new('RGBA', org.size)


    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret1.paste(tab[0], leftT)
    ret2.paste(tab[1], rightT)
    ret3.paste(tab[2], leftB)
    ret4.paste(tab[3], rightB)

    ret = Image.alpha_composite(ret1, ret2)
    ret = Image.alpha_composite(ret, ret3)
    ret = Image.alpha_composite(ret, ret4)

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

def assemble64(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble16(org1[0], [tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8], tab[9], tab[10], tab[11], tab[12], tab[13], tab[14], tab[15]]))
    pic.append(assemble16(org1[1], [tab[16], tab[17], tab[18], tab[19], tab[20], tab[21], tab[22], tab[23], tab[24], tab[25], tab[26], tab[27], tab[28], tab[29], tab[30], tab[31]]))
    pic.append(assemble16(org1[2], [tab[32], tab[33], tab[34], tab[35], tab[36], tab[37], tab[38], tab[39], tab[40], tab[41], tab[42], tab[43], tab[44], tab[45], tab[46], tab[47]]))
    pic.append(assemble16(org1[3], [tab[48], tab[49], tab[50], tab[51], tab[52], tab[53], tab[54], tab[55], tab[56], tab[57], tab[58], tab[59], tab[60], tab[61], tab[62], tab[63]]))

    ret = assemble4(org, pic)

    return ret

d = []
for i in range(1, 65):
    d.append(Image.open('D:\INZ2\INZ9v6\m' + str(i) + '\m' + str(i) + '-199.png').convert("RGBA"))

ideal = Image.open("MonaLisa.png").convert("RGBA")

ass = assemble64(ideal, d)
ass.show()
ass.save("xd.png")