from PIL import Image, ImageDraw
import random

# generate a list of random vertice to draw a polygon
def getVertice(size):
    # random num of vertice for current polygon
    verticeNum = random.randint(3,9)
    vertice = []
    cnt = 0

    while cnt < verticeNum:
        x = random.randint(0, size[0] - 1)
        y = random.randint(0, size[1] - 1)
        vertice.append((x, y))
        cnt += 1
    return vertice

# evole by one generation
def evole(src, dst):
    im = Image.new("RGB", src.size)
    draw = ImageDraw.Draw(im)
    # draw 2-4 random polygons on the new image
    for i in range(1, random.randint(2, 4)):
        coordinates = getVertice(src.size)
        col = (src.getpixel((coordinates[0][0], coordinates[0][1])))
        draw.polygon(coordinates, fill = col)

    # compare the new image, dst image with src image pixel by pixel
    for i in range(0, src.size[0]):
        for j in range(0, src.size[1]):
            # im is more similar with src than dst iff
            # RGB sum of im is closer to that of src than that of dst
            src_sum = sum(src.getpixel((i,j)))
            im_diff = abs(sum(im.getpixel((i,j))) - src_sum)
            dst_diff = abs(sum(dst.getpixel((i,j))) - src_sum)
            if im_diff < dst_diff:
                dst.putpixel((i,j), im.getpixel((i,j)))
    return dst


src = Image.open("MonaLisa.png")
dst = Image.new("RGB", src.size)
iteration = 300

for i in range(1, iteration):
    dst = evole(src, dst)
    name = str(i)
    print(name)
    dst.save("E:/INZ3/" + name+".jpg", "JPEG")

dst.save("E:/INZ3/output.jpg", "JPEG")