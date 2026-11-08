import cv2 as cv
from read import rescaleFrame

img=cv.imread('images/me.png')
# img=rescaleFrame(img,0.2)

cv.imshow('Image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Thresholding
threshold,thres=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thres)

threshold,thres_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse',thres_inv)

#Adaptive Thresholding
adaptive_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive Thresholded',adaptive_thres)


# cv.imwrite('images/me_sketch.png',adaptive_thres)



cv.waitKey(0)

