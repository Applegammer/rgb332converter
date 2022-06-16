from PIL import Image
import sys

im = Image.open('bw_template.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_map = im.load()

# print (width, height)
# print (pixel_values)
# print (pixel_map)

rgb_output = open('test_output.txt', 'w')
for x in range (width):
    for y in range (height):
        print ("position of X: " + str(x) + " position of Y: " + str(y))
        rgb24 = pixel_map [x, y]
        print (rgb24)
        rgb_output.write(str(rgb24) + "," )
rgb_output.close()