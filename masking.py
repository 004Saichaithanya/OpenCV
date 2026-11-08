import cv2 as cv
from read import rescaleFrame
import numpy as np

img=cv.imread('images/me.png')
img=rescaleFrame(img)
cv.imshow('Image',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2 -120),150,255,-1)
rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
weird_shape=cv.bitwise_and(circle,rect)
cv.imshow('Werid ',weird_shape)


masked=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Masked',masked)


cv.waitKey(0)