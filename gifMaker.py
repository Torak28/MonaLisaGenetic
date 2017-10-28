from PIL import Image
import os

path = 'E:/INZ/'
len = len(os.listdir(path))

im = []
Im = Image.open(path + "5001.png")

for i in range(5001,len):
    im.append(Image.open(path + str(i) + ".png"))


imgList = [img for img in im]

Im.save("8bth_run.gif", save_all=True, append_images=imgList, loop=1, duration=10)