import random, operator, math, numpy, os
from PIL import Image, ImageDraw, ImageChops, ImageStat

def crop4(org):
    ret = []
    width, height = org.size

    leftT = 0, 0, width//2 + 10, height//2
    rightT = width//2, 0, width, height//2 + 10
    leftB = 0, height//2 - 10, width//2, height
    rightB = width//2 - 10, height//2, width, height

    ret.append(org.crop(leftT))
    ret.append(org.crop(rightT))
    ret.append(org.crop(leftB))
    ret.append(org.crop(rightB))

    return ret

def assemble4(org, tab):
    ret1 = Image.new('RGBA', org.size, (0, 0, 0, 0))
    ret2 = Image.new('RGBA', org.size, (0, 0, 0, 0))
    ret3 = Image.new('RGBA', org.size, (0, 0, 0, 0))
    ret4 = Image.new('RGBA', org.size, (0, 0, 0, 0))

    width, height = org.size

    leftT = 0, 0, width // 2 + 10, height // 2
    rightT = width // 2, 0, width, height // 2 + 10
    leftB = 0, height // 2 - 10, width // 2, height
    rightB = width // 2 - 10, height // 2, width, height

    ret1.paste(tab[0], leftT)
    ret2.paste(tab[1], rightT)
    ret = Image.alpha_composite(ret2, ret1)
    ret3.paste(tab[2], leftB)
    ret = Image.alpha_composite(ret, ret3)
    ret4.paste(tab[3], rightB)
    ret = Image.alpha_composite(ret, ret4)

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
m = crop4(ideal)
m1 = m[0]
m2 = m[1]
m3 = m[2]
m4 = m[3]

ass = assemble4(ideal, m)

print(distance2(ideal, ass))