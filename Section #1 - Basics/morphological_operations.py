# importing dependencies
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# reading the image and setting up kernel
img=cv.imread('WIN_20220701_11_40_17_Pro.jpg')
kernel = np.ones((5,5),np.uint8) #creates a kernel matrix of size 5x5 filled with ones, using the data type np.uint8
plt.imshow(img)

# Erosion
erosion = cv.erode(img,kernel)
plt.imshow(erosion)

# dilsation

dilation = cv.dilate(img,kernel)
plt.imshow(dilation)