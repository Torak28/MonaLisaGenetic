from PIL import Image
import os

path = 'E:/INZ/'
len = len(os.listdir(path))

im = []
Im = Image.open("2nd_run.gif")

for i in range(len):
    im.append(Image.open(path + str(i) + ".png"))


Im.save("3rd_run.gif", save_all=True, append_images=[img for img in im], loop=1, duration=500)