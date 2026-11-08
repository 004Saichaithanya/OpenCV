import cv2 as cv
import read

img=cv.imread('images/goku.jpg')
img=read.rescaleFrame(img,0.15)
cv.imshow('image',img)

#Average bluring
avg=cv.blur(img,(3,3))
cv.imshow('Avg img',avg)

#Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gauss)

#Median Blur
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral Filter
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)
