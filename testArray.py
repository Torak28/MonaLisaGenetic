import numpy
import math
from PIL import Image, ImageStat

def randomElem():
    ret = numpy.empty([1], int)
    ret = numpy.delete(ret, 0)
    ret = numpy.append(ret, [numpy.random.randint(256, size=4)])
    return ret

def randomPictur(N):
   ret = numpy.empty_like(N)
   for i in range(ret.shape[0]):
       for j in range(ret. shape[1]):
           ret[i][j] = randomElem()
   return ret

def darkPicture(N):
    ret = numpy.zeros_like(N)
    return ret

# distance between 2 oints in 3D space
# |P_1\, P_2| = \sqrt{(x_2- x_1)^2 + (y_2 -y_1)^2 + (z_2- z_1)^2}
def distance(org, N):
    ret = 0
    for i in range(org.shape[0]):
        for j in range(org.shape[1]):
            ret += int(math.sqrt(pow(int(N[i][j][0]) - int(org[i][j][0]),2) + pow(int(N[i][j][1]) - int(org[i][j][1]),2) + pow(int(N[i][j][2]) - int(org[i][j][2]),2)))
    return ret

# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")
# convert to numpy (for convenience)
tab = numpy.asarray(im, dtype='uint8')

test = randomPictur(tab)

print(distance(tab,test))

newIm = Image.fromarray(tab, "RGBA")
newIm.show()
newIm.save("out3.png")