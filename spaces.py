import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import read

img=cv.imread('images/goku.jpg')

img=read.rescaleFrame(img,0.3)
cv.imshow('Me',img)

# # plt.imshow(img)
# # plt.show()

# #BGR to Gray
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# #BGR to HSV
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# #BGR to LAB
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB',lab)

# #BGR to RGB
# rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('RGB',rgb)


# #HSV to BGR

# hsv_b=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow('HSV2BGR',hsv_b)



#Color Channeling

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merged=cv.merge([b,g,r])
# cv.imshow('Merged Image',merged)



cv.waitKey(0)