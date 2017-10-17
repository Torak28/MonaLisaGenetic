from PIL import Image
import numpy

def distance2(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            a = int(org[i][j][0]) + int(org[i][j][1]) + int(org[i][j][2])
            b = int(N[i][j][0]) + int(N[i][j][1]) + int(N[i][j][2])
            ret += (a - b) * (a - b)
    return ret

im = Image.open("MonaLisa.png").convert("RGBA")
tab = numpy.asarray(im, dtype='uint8')

im2 = Image.open("E:\INZ\\176.png").convert("RGBA")
test = numpy.asarray(im2, dtype='uint8')

print("Fitnes wyniku: %s" % distance2(tab, test))


