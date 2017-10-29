from PIL import Image, ImageChops
import numpy
import math, operator

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

def reduce(function, iterable, initializer=None):
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

def rmsdiff_1997(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

img1 = Image.open("MonaLisa.png").convert("RGBA")
img2 = Image.open("E:\INZ\\9999.png").convert("RGBA")
img3 = darkPicture(img1)

dif = rmsdiff_1997(img1, img3)

print(dif)