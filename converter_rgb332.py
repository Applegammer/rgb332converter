from PIL import Image

im = Image.open('black_white.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pix = im.load()