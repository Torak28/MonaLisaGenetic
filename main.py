from PIL import Image, ImageDraw

# Open Lisa and create other image
og = Image.open('MonaLisa.png')
widthOG, heightOG = og.size
black = Image.new('RGB', og.size)

draw = ImageDraw.Draw(black, 'RGBA')
draw.polygon([(50, 0), (100, 100), (0, 100)], (255, 0, 0, 125))
draw.polygon([(50,100), (100, 0), (0, 0)], (0, 255, 0, 125))
del draw

black.show()
# black.save('out.png')