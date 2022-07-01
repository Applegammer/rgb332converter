from PIL import Image

#Part of function from PILLOW library
im = Image.open('rainbow_template.png', 'r')     # Function opens an image from the defined path
width, height = im.size                     # Defined two values witch will be use on the loop to check  pixel by pixel and it take width and height from an image
pixel_map = im.load()                       # Check lines X,Y and get values from an image (e.g pixel 0,0 give 255, 255, 255 RGB palette)

#Program section
rgb_output = open('test_output.txt', 'w')                                       # Value which create a text file, where will be store output data
for y in range (height):                                                        # For x lines from 0 to end height of an image
    for x in range (width):                                                     # For y lines from 0 to end width of an image
        r, g, b = pixel_map [x, y]                                              # Value store RGB palett (r - red, g - green, b - blue)
        r3 = int(r / 32)                                                        # Change red value from 24-bit to 8 bit (3 bit for red)
        g3 = int(g / 32)                                                        # Change green value from 24-bit to 8 bit (3 bit for green)
        b2 = int(b / 64)                                                        # Change blue value from 24-bit to 8 bit (3 bit for blue)
        # rgb332 = (r3, g3, b2)                                                 # Value store RGB332 palett
        bin_r = bin(r3)[2:].zfill(3)                                            # Lines [17-19] change red, green, blue value to binary 
        bin_g = bin(g3)[2:].zfill(3)                                            # [2:] remove '0b' from value, after convert to binary
        bin_b = bin(b2)[2:].zfill(2)                                            # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
        binary_rgb = (bin_r, bin_g, bin_g)
        rgb_output.write(str(binary_rgb) + ", " )                               # Store output values to a file
rgb_output.close()                                                              # Close file after loop end, there is end of program, last line.