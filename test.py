import numpy
from PIL import Image, ImageDraw, ImageStat

# read image as RGB and add alpha (transparency)
im = Image.open("MonaLisa.png").convert("RGBA")

# convert to numpy (for convenience)
imArray = numpy.asarray(im)

# create mask
polygon = [(50,0),(100,100),(0,100)]
maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
mask = numpy.array(maskIm)

# assemble new image (uint8: 0-255)
newImArray = numpy.empty(imArray.shape,dtype='uint8')

# colors (three first columns, RGB)
newImArray[:,:,:3] = imArray[:,:,:3]

# transparency (4th column)
newImArray[:,:,3] = mask*255

# back to Image from numpy
newIm = Image.fromarray(newImArray, "RGBA")
newIm.save("out.png")

average = ImageStat.Stat(Image.open("out.png")).median
newI = Image.new('RGB', newIm.size, tuple(average))
newI.save('out2.png')
