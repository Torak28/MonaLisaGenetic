import numpy
from PIL import Image

# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")

# convert to numpy (for convenience)
tab = numpy.asarray(im)

#f = open('test.txt', 'w')
#for item in tab:
#    f.write("%s\n" %item)
#f.close()

print(tab[0][0][0])