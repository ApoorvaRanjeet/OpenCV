import cv2 as cv

# Reading the image
img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')
cv.imshow('Apoorva',img)
cv.waitKey(0)
cv.destroyAllWindows()

if img is None:
    print('could not open image',img)
    exit(0)

blur_img = cv.medianBlur(img,23)
cv.imshow('blur image',blur_img)
cv.waitKey(0)
cv.destroyAllWindows()