import cv2 as cv

# img = cv.imread('WIN_20220701_11_40_17_Pro.jpg')

# resized_img=rescaleFrame(img)

# cv.imshow('Apoorva',img)
# cv.imshow('resized image',resized_img)

# cv.waitKey(0)

def  rescaleFrame(frame,scale=.75):
    # this function works for image , videos , and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# Live Video
  # this function works only for live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('WIN_20221027_00_13_40_Pro.mp4')

while True:

    isTrue , frame =capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('resized video',frame_resized)
    if cv.waitKey(20)& 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()