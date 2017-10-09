import numpy
from random import randint
from PIL import Image

# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")

# convert to numpy (for convenience)
tab = numpy.asarray(im)

#f = open('test.txt', 'w')
#for item in tab:
#    f.write("%s\n" %item)
#f.close()

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

newIm = Image.fromarray(randomPictur(tab), "RGBA")
newIm.save("out3.png")