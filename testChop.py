from PIL import Image, ImageChops, ImageStat, ImageDraw
import numpy
import math, operator

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

def find_median_color(N,tup1, tup2):
    tmp = Image.new('L', N.size)
    ret = ImageDraw.Draw(tmp)

    ret.rectangle((tup1, tup2), outline= 1, fill=1)
    median = ImageStat.Stat(N, mask=tmp).median
    return median

img1 = Image.open("MonaLisa.png").convert("RGBA")

dif = find_median_color(img1,(10,10),(100,100))

print(dif)