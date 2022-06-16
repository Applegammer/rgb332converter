from PIL import Image

im = Image.open('bw_template.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_map = im.load()

# print (width, height)
# print (pixel_values)
# print (pixel_map)

for x in range (10):
    for y in range (10):
        print ("position of X: " + str(x) + " position of Y: " + str(y))