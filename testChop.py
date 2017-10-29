from PIL import Image, ImageChops, ImageStat
import numpy
import math, operator

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

def find_median_color(N):
    median = ImageStat.Stat(N).median
    new_image = Image.new("RGBA", N.size, tuple(median))
    return new_image


img1 = Image.open("MonaLisa.png").convert("RGBA")
img2 = Image.open("E:\INZ\\9999.png").convert("RGBA")
img3 = Image.fromarray(darkPicture(img1), "RGBA")

dif = find_median_color(img1)

dif.show()