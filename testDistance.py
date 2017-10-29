from PIL import Image, ImageChops
import numpy
import math, operator
import time

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

def distance(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            ret += int(math.sqrt(pow(int(N[i][j][0]) - int(org[i][j][0]),2) + pow(int(N[i][j][1]) - int(org[i][j][1]),2) + pow(int(N[i][j][2]) - int(org[i][j][2]),2)))
    return ret

# suma różnic kwadratów
def distance2(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            a = int(org[i][j][0]) + int(org[i][j][1]) + int(org[i][j][2])
            b = int(N[i][j][0]) + int(N[i][j][1]) + int(N[i][j][2])
            ret += (a - b) * (a - b)
    return ret

def distance3(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            deltaR = int(org[i][j][0]) - int(N[i][j][0])
            deltaG = int(org[i][j][1]) - int(N[i][j][1])
            deltaB = int(org[i][j][2]) - int(N[i][j][2])

            pFit = deltaR * deltaR + deltaG * deltaG + deltaB * deltaB
            ret += pFit
    return ret

def distance4(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            if org[i][j][0] != N[i][j][0] or org[i][j][1] != N[i][j][1] or org[i][j][2] != N[i][j][2]:
                ret +=1
    return ret

def distance5(org, N):
    org = Image.fromarray(org, "RGBA")
    N = Image.fromarray(N, "RGBA")
    diff1 = ImageChops.subtract(org, N)
    return (numpy.sum(numpy.asarray(diff1, dtype='uint8')))

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

def distance6(org, N):
    "Calculate the root-mean-square difference between two images"\
    "http://effbot.org/zone/pil-comparing-images.htm"

    org = Image.fromarray(org, "RGBA")
    N = Image.fromarray(N, "RGBA")

    h = ImageChops.difference(org, N).histogram()

    # calculate rms
    ret =  math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(org.size[0]) * org.size[1]))

    return int(ret)

def checkDistancFunc(func):
    im = Image.open("MonaLisa.png").convert("RGBA")
    tab = numpy.asarray(im, dtype='uint8')

    im2 = Image.open("out.png").convert("RGBA")
    test = numpy.asarray(im2, dtype='uint8')

    im3 = Image.open("E:\INZ\\9999.png").convert("RGBA")
    test2 = numpy.asarray(im3, dtype='uint8')

    dark = darkPicture(tab)

    s_x1 = time.time()
    x1 = func(tab, tab)
    k_x1 = time.time() - s_x1
    s_x2 = time.time()
    x2 = func(tab, dark)
    k_x2 = time.time() - s_x2
    s_x3 = time.time()
    x3 = func(tab, test)
    k_x3 = time.time() - s_x3
    s_x4 = time.time()
    x4 = func(tab, test2)
    k_x4 = time.time() - s_x4
    x5 = (x1 * 100) / x2
    x6 = (x2 * 100) / x2
    x7 = (x3 * 100) / x2
    x8 = (x4 * 100) / x2
    print("Funkcja: " + str(func.__name__))
    print("Fitnes wyniku (org): %s (%s)" % (x1, str(math.floor(x5)) + "%"))
    print("Fitnes wyniku (drk): %s (%s)" % (x2, str(math.floor(x6)) + "%"))
    print("Fitnes wyniku (out): %s (%s)" % (x3, str(math.floor(x7)) + "%"))
    print("Fitnes wyniku (bst): %s (%s)" % (x4, str(math.floor(x8)) + "%"))
    print("Średni czas wyniku: %s" % ((k_x1 + k_x2 + k_x3 + k_x4)/4))

    print("---")


checkDistancFunc(distance)
checkDistancFunc(distance2)
checkDistancFunc(distance3)
checkDistancFunc(distance4)
checkDistancFunc(distance5)
checkDistancFunc(distance6)