# Importing dependencies
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# reading image
img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')

# Translation:-> is basically shifting an image along the x,y axis

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])   # width and height of the image
    return cv.warpAffine(img,transmat,dimensions)

# -x ---> left
# -y ---> up
# x ---> right
# y ---> down

translated = translate(img,100,100)

cv.imshow('translated',translated)

# Rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[0],img.shape[1]
    
    # if rotPoint is none we are going to assume that image will rotate from center
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotmat=cv.getRotataionMatrix2D(rotPoint,angle,1.0)     # 1.0 is the scale value
    dimensions = (width,height)
    return cv.warpAffine(img,rotmat,dimensions)

rotated = rotate(img,45)
cv.imshow('rotated',rotated)


## resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image',resize)

cv.waitKey(0)