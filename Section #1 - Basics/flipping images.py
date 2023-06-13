# IMPORT STATEMENTS

import cv2 as cv
from matplotlib import pyplot as plt

# READING THE IMAGE

img= cv.imread('WIN_20220701_11_40_17_Pro.jpg')
cv.imshow('Apoorva',img)
cv.waitKey(0)

# FLIPPING THE IMAGE HORIZONTALLY 

horizontal_flip = cv.flip(img,1)
cv.imshow('horizontal image',horizontal_flip)
cv.waitKey(0)

#FLIPPING THE IMAGE VERTICALLY

vertical_flip = cv.flip(img,0)
cv.imshow('vertical image',vertical_flip)
cv.waitKey(0)

# FLIPPING THE IMAGE VERTICALLY AND HORIZONTALLY
horizontal_vertical_flip = cv.flip(img,-1)
cv.imshow('horizontal and vertical image',horizontal_vertical_flip)
cv.waitKey(0)