from PIL import Image
import os

path = 'D:/INZ2/INZ10v8/'
len = len(os.listdir(path))

im = []
Im = Image.open(path + os.listdir(path)[0])

for i in range(len):
    if not os.listdir(path)[i].endswith(".txt"):
        im.append(Image.open(path + os.listdir(path)[i]))


imgList = [img for img in im]

Im.save("8th_run.gif", save_all=True, append_images=imgList, loop=0, duration=10)