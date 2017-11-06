from PIL import Image, ImageChops, ImageStat, ImageDraw

img1 = Image.open("MonaLisa.png").convert("RGBA")
img2 = Image.open("F:\INZ8v5\\output.png").convert("RGBA")

h = ImageChops.subtract(img1, img2).show()