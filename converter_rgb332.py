from PIL import Image
from tkinter import filedialog as window

def im_load():
    #Open dialog box to load an image with selected path, from your computer
    open_box = window.askopenfilename(initialdir=".", title="Open file", filetypes=[("PNG files", "*.png")])
    return open_box

def file_save():
    #Open dialog box to save an file with selected path from your computer
    save_box = window.asksaveasfilename(initialdir=".", title="Save file", filetypes=[("TXT file", "*.txt")])
    return save_box

def im_open(image_load):
    #Load image
    im = Image.open(image_load, 'r')                                                # Function opens an image from the defined path.
    pixel_map = im.load()                                                           # Allocates storage for the image and loads the pixel data (e.g pixel 0,0 give 255, 255, 255 RGB palette).
    return im.width, im.height, pixel_map                                           

def convert_rgb_to_rgb332(image_load, path_file):
    #Convert, and save output to .txt file

    width, height, pixel_map = im_open(image_load)

    rgb_output = open(path_file , 'w')                                              # Value which create a text file, where will be store output data.
    for y in range (height):                                                        # For x lines from 0 to end height of an image.
        for x in range (width):                                                     # For y lines from 0 to end width of an image.
            r, g, b = pixel_map [x, y]                                              # Value store RGB palett (r - red, g - green, b - blue).
            r3 = int(r / 32)                                                        # Change red value from 24-bit to 8 bit (3 bit for red).
            g3 = int(g / 32)                                                        # Change green value from 24-bit to 8 bit (3 bit for green).
            b2 = int(b / 64)                                                        # Change blue value from 24-bit to 8 bit (2 bit for blue).
            bin_r = bin(r3)[2:].zfill(3)                                            # Lines [17-19] change red, green, blue value to binary.
            bin_g = bin(g3)[2:].zfill(3)                                            # [2:] remove '0b' from value, after convert to binary.
            bin_b = bin(b2)[2:].zfill(2)                                            # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
            bin_string = bin_r + bin_g + bin_b                                      # Marged three binary values to the one, finally have 8 - bit value.
            rgb_dec = int(bin_string, 2)                                            # Convert binary to decimal system.
            rgb_output.write(str(rgb_dec) + ", ")                                   # Store output values to a file.
    rgb_output.close()                                                              # Close file after loop end, there is end of program, last line.

def program_menu():
    #Simple menu with options to execute
    
    try:
        while True:
            
            print(' Converter RGB to RGB332:')
            print(' [1] -- Select an image --')
            print(' [2]  -- Save as a file --')
            print(' [3]   -- Exit program --')

            option = input(' Please choose an option [1-3]: ')

            if option == '1':
                
                try:
                    print(' [First option has selected]')
                    im_path = im_load()
                    print('\n [INFO]: Image has loaded from: ' + im_path + '\n')
                except TypeError:
                    print()
                    print(' [WARN]: Please choose an image to load \n')

            elif option == '2':
                
                try:
                    print(' [Second option has selected]')
                    save_output = file_save()
                    convert_rgb_to_rgb332(im_path, save_output) 
                    print('\n [INFO]: File has saved in: ' + save_output + '\n')
                except TypeError:
                    print()
                    print(' [WARN]: Something went wrong, please try again \n')
                
                except UnboundLocalError:
                    print()
                    print(' [WARN]: No data to save, please load image first to the program \n')
                
                except AttributeError:
                    print()
                    print(' [WARN]: No data to save, please load image first to the program  \n')

            elif option == '3':
                
                print(' Third option has selected')
                print('\n [INFO]: Program has closed \n')
                exit()

            else:

                print('\n [WARNING]: Something went wrong, please choose option again \n')

    except EOFError:
        print()
        print(' [ERROR]: Unexpected action in program')
    except KeyboardInterrupt:
        print()
        print(' [INFO]: Program has closed unexpected  ')
        exit()
            
msg = open("non-GUI/logo", "r")
print(msg.read())

program_menu()