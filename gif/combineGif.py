from PIL import Image

path = '8ath_run.gif'

im = []
Im = Image.open(path)

Im2 = Image.open('8ath_run.gif')
Im3 = Image.open('8bth_run.gif')

im.append(Im2)
im.append(Im3)

imgList = [img for img in im]

Im.save("8th_run.gif", save_all=True, append_images=imgList, loop=1, duration=10)