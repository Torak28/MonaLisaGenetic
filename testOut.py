from PIL import Image
import numpy
import math

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

def checkDistancFunc(func):
    im = Image.open("MonaLisa.png").convert("RGBA")
    tab = numpy.asarray(im, dtype='uint8')

    im2 = Image.open("out.png").convert("RGBA")
    test = numpy.asarray(im2, dtype='uint8')

    im3 = Image.open("E:\INZ\\9999.png").convert("RGBA")
    test2 = numpy.asarray(im3, dtype='uint8')

    dark = darkPicture(tab)

    x1 = func(tab, dark)
    x2 = func(tab, test)
    x3 = func(tab, test2)
    x4 = (x2 * 100) / x1
    x5 = (x3 * 100) / x1
    print("Funkcja: " + str(func.__name__))
    print("Fitnes wyniku (drk): %s (%s)" % (x1, "100%"))
    print("Fitnes wyniku (out): %s (%s)" % (x2, str(math.floor(x4)) + "%"))
    print("Fitnes wyniku (bst): %s (%s)" % (x3, str(math.floor(x5)) + "%"))

    print("---")


checkDistancFunc(distance)
checkDistancFunc(distance2)
checkDistancFunc(distance3)
checkDistancFunc(distance4)