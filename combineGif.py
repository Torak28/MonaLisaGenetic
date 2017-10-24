from PIL import Image
import os

path = '8th_run.gif'

im = []
Im = Image.open(path)

Im2 = Image.open('9th_run.gif')
Im3 = Image.open('10th_run.gif')

im.append(Im2)
im.append(Im3)

imgList = [img for img in im]

Im.save("11th_run.gif", save_all=True, append_images=imgList, loop=1, duration=10)