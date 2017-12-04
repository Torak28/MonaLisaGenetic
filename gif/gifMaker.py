from PIL import Image
import os

path = 'E:/INZ4/'
len = len(os.listdir(path))

im = []
Im = Image.open(path + "0.png")

for i in range(len):
    im.append(Image.open(path + str(i) + ".png"))


imgList = [img for img in im]

Im.save("9th_run.gif", save_all=True, append_images=imgList, loop=1, duration=10)