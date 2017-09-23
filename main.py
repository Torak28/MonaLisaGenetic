from PIL import Image

# Open Lisa and create other image
og = Image.open('MonaLisa.png')
widthOG, heightOG = og.size
black = Image.new('RGB', (widthOG, heightOG), 255)
black.show()
black.save('out.png')