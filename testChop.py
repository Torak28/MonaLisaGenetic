from PIL import Image, ImageChops, ImageStat, ImageDraw

img1 = Image.open("MonaLisa.png").convert("RGBA")
img2 = Image.open("E:\INZ5v3\\29416.png").convert("RGBA")

h = ImageChops.subtract(img1, img2).show()