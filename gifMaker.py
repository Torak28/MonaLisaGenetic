from PIL import Image
import os

path = 'E:/INZ3/'
len = len(os.listdir(path))

im = []
Im = Image.open(path + "201.jpg")

for i in range(202,len):
    im.append(Image.open(path + str(i) + ".jpg"))


imgList = [img for img in im]

Im.save("10th_run.gif", save_all=True, append_images=imgList, loop=1, duration=10)