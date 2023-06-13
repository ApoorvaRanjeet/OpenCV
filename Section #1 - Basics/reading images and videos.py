import cv2 as cv

#reading images in opencv

# img=cv.imread('WIN_20220701_11_40_17_Pro.jpg')
# cv.imshow('Apoorva',img)
# cv.waitKey(0)


#reading videos in opencv

capture = cv.VideoCapture('WIN_20221027_00_13_40_Pro.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # which basicallymeans that if letter d is pressed then it will break out of the while loop
        break
capture.release()
cv.destroyAllWindows()    