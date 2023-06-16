#Import statements
import cv2 as cv
import random
from matplotlib import pyplot as plt

# FUNCTION DEFINATION

# function add_noise() fro adding random black and white pixels
#this function will create a sprinkled salt and pepper effect on the picture.

def add_noise(img):
    row,col = img.shape
    number_of_pixels = random.randint(300,10000)
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[xcord,ycord]=255
    number_of_pixels = random.randint(300,10000)
    for i in range(number_of_pixels):
        ycord=random.randint(0,row-1)
        xcord=random.randint(0,col-1)
        img[xcord,ycord]=0
    return img    
    
# CODE TO READ IMAGE

img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')
plt.imshow('Apoorva',img)
plt.show

img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow('Apoorva',img_rgb)
plt.show

