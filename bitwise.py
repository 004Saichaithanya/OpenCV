import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rect)
cv.imshow('Circle',circle)

#Bitwise And
#Only intersecting regions
bitwise_and=cv.bitwise_and(rect,circle)
cv.imshow('Bitwise And',bitwise_and)

#bitwise OR
# both intersecting and non-intersecting regions
bitwise_or=cv.bitwise_or(rect,circle)
cv.imshow('Bitwise OR',bitwise_or)

#bitwise XOR
#only non-intersecting regions
bitwise_xor=cv.bitwise_xor(rect,circle)
cv.imshow('bitwise XOR',bitwise_xor)

#bitwise NOT
bitwise_not_rect=cv.bitwise_not(rect)
cv.imshow('Rect Not',bitwise_not_rect)

bitwise_not_circle=cv.bitwise_not(circle)
cv.imshow('circle Not',bitwise_not_circle)

cv.waitKey(0)


