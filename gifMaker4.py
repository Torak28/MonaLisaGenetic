from PIL import Image
import os

from PIL import Image

def combine(g1, g2, strx):
    im = []

    Im = Image.open('gif/tmp/Open.png')

    Im2 = Image.open('gif/tmp/' + str(g1) + '.gif')
    Im3 = Image.open('gif/tmp/' + str(g2) + '.gif')

    im.append(Im2)
    im.append(Im3)

    imgList = [img for img in im]

    Im.save("gif/tmp/" + str(strx) + ".gif", save_all=True, append_images=imgList, loop=1, duration=1)

    Im2.close()
    Im3.close()

    os.remove('gif/tmp/' + str(g1) + '.gif')
    os.remove('gif/tmp/' + str(g2) + '.gif')


def assemble4(org, tab):
    ret = Image.new('RGBA', org.size, (0, 0, 0, 255))
    width, height = org.size

    leftT = 0, 0, width // 2, height // 2
    rightT = width // 2, 0, width, height // 2
    leftB = 0, height // 2, width // 2, height
    rightB = width // 2, height // 2, width, height

    ret.paste(tab[0], leftT)
    ret.paste(tab[1], rightT)
    ret.paste(tab[2], leftB)
    ret.paste(tab[3], rightB)

    return ret

def makeGif4(pocz, kon, path, strx):
    org = Image.open("MonaLisa.png").convert("RGBA")
    numDir = 0
    for i in range(len(os.listdir(path))):
        if os.path.isdir(path + os.listdir(path)[i]):
            numDir += 1
    length = len(os.listdir(path + "m1"))

    im = []
    ImTab = []
    for i in range(numDir):
        ImTab.append(Image.open(path + "m" + str(i+1) + "/m" + str(i+1) + "-" + str(pocz) + ".png").convert("RGBA"))


    # Zdjęcie otwierajace
    Im = assemble4(org, ImTab)
    if(pocz == 0):
        Im.save("gif/tmp/Open.png")

    for i in range(pocz, kon):
        xd = []
        for j in range(numDir):
            xd.append(Image.open(path + "m" + str(j + 1) + "/m" + str(j + 1) + "-" + str(i) + ".png").convert("RGBA"))
        im.append(assemble4(org, xd))


    imgList = [img for img in im]

    Im.save("gif/tmp/" + str(strx) + ".gif", save_all=True, append_images=imgList, loop=1, duration=1)

def clear(N, strx):
    os.rename('gif/tmp/' + str(N) + '.gif', 'gif/' + str(strx) + 'th_tun.gif')
    os.remove('gif/tmp/Open.png')
    os.rmdir('gif/tmp')

def prepare():
    os.makedirs('gif/tmp')

# Zmienna
path = 'F:/INZ6v4/'

prepare()

makeGif4(0, 1000, path, 1)
makeGif4(1001, 2000, path, 2)
makeGif4(2001, 3000, path, 3)
makeGif4(3001, 4000, path, 4)
makeGif4(4001, 5000, path, 5)
makeGif4(5001, 6000, path, 6)
makeGif4(6001, 7000, path, 7)
makeGif4(7001, 8000, path, 8)
makeGif4(8001, 9000, path, 9)
makeGif4(9001, 10000, path, 10)

combine(1, 2, 11)
combine(11, 3, 12)
combine(12, 4, 13)
combine(13, 5, 14)
combine(14, 6, 15)
combine(15, 7, 16)
combine(16, 8, 17)
combine(17, 9, 18)
combine(18, 10, 19)

clear(19, 10)
