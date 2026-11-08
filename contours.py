import cv2 as cv
import numpy as np
import read
img=cv.imread('images/me.png')
img=read.rescaleFrame(img,0.5)
cv.imshow('Me',img)

blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

canny=cv.Canny(img,125,175)
# cv.imshow('Canny',canny)

# ret,thres=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thres',thres)

contours,hierachies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} coutours found!')


cv.drawContours(blank,contours,-1,(255,255,0),1)
cv.imshow('Coutoured',blank)



cv.waitKey(0)