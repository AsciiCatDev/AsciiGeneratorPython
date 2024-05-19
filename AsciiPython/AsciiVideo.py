#This code is written by Ascii Cat Devs and is used for creating ascii videos from mp4 files
#it works best with high contrast low resolution videos

import numpy as np
import cv2 as cv
import text_to_image
from PIL import Image

# Define ASCII characters to represent different intensity levels
# adjust these to get different effects 
ASCII_CHARS = "@#a*+=!:-,._        " #better for bright background
#ASCII_CHARS = "     _.,-:!=+*a#@" #better for dark background
#ASCII_CHARS = "    @*@*@*     "

AsciiImages = []
############# IMPORTANT ###################
video = cv.VideoCapture('img/spinner.mp4') #change this video with whatever video you want to convert to ascii

# Define video properties
fps = 24 
filename = input("Enter desired file name, (Dont Include Type mp4 automatically added)\n")   
output_file = filename.strip() + '.mp4'
# Initialize video writer
fourcc = cv.VideoWriter_fourcc(*'mp4v')
#we need to import text to pixel class to convert the ascii characters back into pixels 
t2p = text_to_image.TextToPixel()

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
pixel_to_ascii

##### MAIN ################################
# this part goes frame by frame and converts it to ascii
while video.isOpened():
    ret, frame = video.read()

    # if frame is read correctly ret is True
    if not ret:
        print("loading...")
        break

#################### IMPORTANT #################
    tempImage = resize_image(frame, 50) #adjust this to change the resolution
################################################3
    tempImage = pixel_to_ascii(tempImage)
    AsciiImages.append(tempImage)
video.release()

image = t2p.create_img(AsciiImages[0]) 
imageArray = cv.cvtColor(np.array(image), cv.COLOR_RGBA2GRAY)
frame_size = (imageArray.shape[1], imageArray.shape[0])
video_writer = cv.VideoWriter(output_file, fourcc, fps, frame_size, isColor=False)

#now we convert array of strings or ascii images to video 
for ascii_image in AsciiImages:
    # Convert ASCII image to grayscale OpenCV image
    image = t2p.create_img(ascii_image) 
    imageArray = cv.cvtColor(np.array(image), cv.COLOR_RGBA2GRAY)
    #image = ascii_to_image(ascii_image, width, height)
    video_writer.write(imageArray)

# Release the video writer
video_writer.release()

print("num of frames: " + str(len(AsciiImages)))
print("Video saved as:", output_file)

 
