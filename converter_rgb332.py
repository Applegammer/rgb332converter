from PIL import Image

#Part of function from PILLOW library
im = Image.open('bw_template.png', 'r')     # Function opens an image from the defined path
width, height = im.size                     # Defined two values witch will be use on the loop to check  pixel by pixel and it take width and height from an image
pixel_map = im.load()                       # Check lines X,Y and get values from an image (e.g pixel 0,0 give 255, 255, 255 RGB palette)

#Program section
rgb_output = open('test_output.txt', 'w')                                       # Value which create a text file, where will be store output data
for x in range (width):                                                         # For x lines from 0 to end height of an image
    for y in range (height):                                                    # For y lines from 0 to end width of an image
        # print ("position of X: " + str(x) + " position of Y: " + str(y))      # Values to debugging if loop works properly
        rgb24 = pixel_map [x, y]                                                # Value store RGB palett
        # print (rgb24)                                                         # Values to debbugging if RGB output from pixels are correctly
        rgb_output.write(str(rgb24) + "," )                                     # Store output values to a file
rgb_output.close()                                                              # Close file after loop end