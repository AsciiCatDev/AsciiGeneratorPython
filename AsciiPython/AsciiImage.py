#This code is written by Ascii Cat Devs and is used for creating ascii images from jpg files
#it works best with high contrast low resolution images

import numpy as np
import cv2 as cv
import text_to_image
from PIL import Image

# Define ASCII characters to represent different intensity levels
# adjust these to get different effects 
#ASCII_CHARS = "@a+*!:-,._    " #better for bright background
ASCII_CHARS = " _.,-:!=+*a#@"   #better for dark background
#ASCII_CHARS = "    @*@*@*     "

# Resize the image to desired width while maintaining aspect ratio
def resize_image(image, new_width=100):
    ratio = float(new_width) / image.shape[1]
    new_height = int(image.shape[0] * ratio) 
    resized_image = cv.resize(image, (int(new_width), new_height))
    return resized_image

# Convert each pixel to ASCII character based on intensity
def pixel_to_ascii(image):
    ascii_image = ''
    for row in image:
        for pixel in row:
            grayscale_value = pixel[0]
            ascii_image += ASCII_CHARS[int(grayscale_value / 256 * len(ASCII_CHARS))]
        ascii_image += '\n'
    return ascii_image

##### IMPORTANT ################################
img = cv.imread('img/cat.jpg') #change royalCat.jpg with the name of the image you want to convert
######################################

filename = input("Enter desired file name, (Dont Include Type, PNG automatically added)\n") # name your file
output_file = filename.strip() + '.png'

t2p = text_to_image.TextToPixel() #convert ascii string to actual png image

################ IMPORTANT #########################
tempImage = resize_image(img, 100) # adjust this number to increase or decrease resolution of ascii art
####################################################

tempImage = pixel_to_ascii(tempImage) 
image = t2p.create_img(tempImage) 
image.save(output_file)
image.show()

print("image saved as:", output_file)

