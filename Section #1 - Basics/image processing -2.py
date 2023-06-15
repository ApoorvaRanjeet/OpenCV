import cv2 as cv
import numpy as np

# reading the image
img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')
cv.imshow('Apoorva',img)
cv.waitKey(0)

# Splitting image into RGB channel
blue, green, red = cv.split(img)
# Displaying each of them

cv.imshow('blue grayscale',blue)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('red grayscale',red)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('green grayscale',green)
cv.waitKey(0)
cv.destroyAllWindows()