import cv2 as cv
import numpy as np
import read 

img=cv.imread('images/goku.jpg')
img=read.rescaleFrame(img,0.2)

cv.imshow('Image',img)


#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dims=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dims)

# -x --> left
# -y -->Up
# x -->right
# y -->down

translated=translate(img,-100,-100)
# cv.imshow('Translate',translated)

#Rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dims=(width,height)
    return cv.warpAffine(img,rotMat,dims)


rotated=rotate(img,45)
# cv.imshow('Rotated',rotated)

rotated45=rotate(rotated,45)
# cv.imshow('Rotated45',rotated45)


#Resizing

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

#Flipping
#Flipcode
# 0-->vertically/x-axis
# 1 --> horizontally/y-axis
# -1 --> both

flipped=cv.flip(img,-1)
cv.imshow('Flipped',flipped)



#Cropping

cropped=img[200:500,400:600]
cv.imshow('Crop',cropped)


cv.waitKey(0)
