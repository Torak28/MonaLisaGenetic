import operator, math
from PIL import Image, ImageChops

def crop256(org):
    ret64 = crop64(org)

    ret256 = crop4(ret64[0])
    for _ in range(1, 64):
        ret256.extend((crop4(ret64[_])))

    return ret256

def crop64(org):
    ret16 = crop16(org)

    ret64 = crop4(ret16[0])
    for _ in range(1,16):
        ret64.extend(crop4(ret16[_]))

    return ret64

def crop16(org):
    ret4 = crop4(org)
    ret16 = crop4(ret4[0])
    ret16.extend(crop4(ret4[1]))
    ret16.extend(crop4(ret4[2]))
    ret16.extend(crop4(ret4[3]))

    return ret16

def assemble256(org, tab):

    org1 = crop4(org)

    pic = []

    pic.append(assemble64(org1[0], tab[:64]))
    pic.append(assemble64(org1[0], tab[64:128]))
    pic.append(assemble64(org1[0], tab[128:192]))
    pic.append(assemble64(org1[0], tab[192:256]))

    ret = assemble4(org, pic)

    return ret

def assemble64(org, tab):
    org1 = crop4(org)

    pic = []

    pic.append(assemble16(org1[0], tab[:16]))
    pic.append(assemble16(org1[1], tab[16:32]))
    pic.append(assemble16(org1[2], tab[32:48]))
    pic.append(assemble16(org1[3], tab[48:64]))

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
m = crop256(ideal)

ass = assemble256(ideal, m)

print(distance2(ideal, ass))