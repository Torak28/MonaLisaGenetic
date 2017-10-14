import numpy
import math
from PIL import Image

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

# Mutacja
def square(org, N):
    tmp = darkPicture(N)
    x = numpy.random.randint(org.shape[0])
    y = numpy.random.randint(org.shape[1])
    w = numpy.random.random_integers(x + 1,org.shape[0])
    h = numpy.random.random_integers(y + 1, org.shape[1])
    R = org[x][y][0]
    G = org[x][y][1]
    B = org[x][y][2]
    A = numpy.random.randint(256)
    for i in range(N.shape[0]):
        if i >= x and i <= w:
            for j in range(N.shape[1]):
                if j >=y and j <= h:
                    tmp[i][j][0] = R
                    tmp[i][j][1] = G
                    tmp[i][j][2] = B
                    tmp[i][j][3] = A
    ret = Image.alpha_composite(Image.fromarray(N,"RGBA"),Image.fromarray(tmp,"RGBA"))
    return numpy.asarray(ret, dtype='uint8')



# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")
# convert to numpy (for convenience)
tab = numpy.asarray(im, dtype='uint8')

test = darkPicture(tab)
for i in range(300):
    test = square(tab, test)

newIm = Image.fromarray(test, "RGBA")
newIm.show()

#newIm.save("out3.png")