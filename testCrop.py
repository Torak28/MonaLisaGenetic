import operator, math
from PIL import Image, ImageChops

def crop64(org):
    ret4 = crop4(org)

    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    ret64 = crop4(ret16[0])
    ret64.extend(crop4(ret16[1]))
    ret64.extend(crop4(ret16[2]))
    ret64.extend(crop4(ret16[3]))
    ret64.extend(crop4(ret16[4]))
    ret64.extend(crop4(ret16[5]))
    ret64.extend(crop4(ret16[6]))
    ret64.extend(crop4(ret16[7]))
    ret64.extend(crop4(ret16[8]))
    ret64.extend(crop4(ret16[9]))
    ret64.extend(crop4(ret16[10]))
    ret64.extend(crop4(ret16[11]))
    ret64.extend(crop4(ret16[12]))
    ret64.extend(crop4(ret16[13]))
    ret64.extend(crop4(ret16[14]))
    ret64.extend(crop4(ret16[15]))

    return ret64

def crop16(org):
    ret4 = crop4(org)
    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    return ret16

def assemble64(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble16(org1[0], [tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8], tab[9], tab[10], tab[11], tab[12], tab[13], tab[14], tab[15]]))
    pic.append(assemble16(org1[1], [tab[16], tab[17], tab[18], tab[19], tab[20], tab[21], tab[22], tab[23], tab[24], tab[25], tab[26], tab[27], tab[28], tab[29], tab[30], tab[31]]))
    pic.append(assemble16(org1[2], [tab[32], tab[33], tab[34], tab[35], tab[36], tab[37], tab[38], tab[39], tab[40], tab[41], tab[42], tab[43], tab[44], tab[45], tab[46], tab[47]]))
    pic.append(assemble16(org1[3], [tab[48], tab[49], tab[50], tab[51], tab[52], tab[53], tab[54], tab[55], tab[56], tab[57], tab[58], tab[59], tab[60], tab[61], tab[62], tab[63]]))

    ret = assemble4(org, pic)

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


def crop4(org):
    ret = []
    width, height = org.size

    leftT = 0, 0, width//2, height//2
    rightT = width//2, 0, width, height//2
    leftB = 0, height//2, width//2, height
    rightB = width//2, height//2, width, height

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

    ret.paste(tab[0], leftT, mask=tab[0])
    ret.paste(tab[1], rightT, mask=tab[1])
    ret.paste(tab[2], leftB, mask=tab[2])
    ret.paste(tab[3], rightB, mask=tab[3])

    return ret

def reduce(function, iterable, initializer=None):
    "Funkcja z Pythona 2.7"
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

def distance2(org, N):
    "Calculate the root-mean-square difference between two images"\
    "http://effbot.org/zone/pil-comparing-images.htm"

    h = ImageChops.difference(org, N).histogram()

    # calculate rms
    ret =  math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(org.size[0]) * org.size[1]))

    return ret

ideal = Image.open("MonaLisa.png").convert("RGBA")
m = crop64(ideal)

ass = assemble64(ideal, m)

print(distance2(ideal, ass))