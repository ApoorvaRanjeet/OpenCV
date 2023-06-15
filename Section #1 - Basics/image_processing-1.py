# convert color image to gray scale

# importing statements
import cv2 as cv

# Reading the image
img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')
cv.imshow('Apoorva',img)
cv.waitKey(0)
cv.destroyAllWindows()

if img is None:
    print('could not open image',img)
    exit(0)

#grayscale version of the input image
img_grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('grayscaled image',img_grayscale)
cv.waitKey(0)
cv.destroyAllWindows()
