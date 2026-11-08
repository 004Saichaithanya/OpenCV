import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')

# img=cv.imshow('blank',blank)

#paint the color 

# blank[200:300,300:400]=200,255,23
# cv.imshow('green',blank)

#draw a rect

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]),(500,250,23),thickness=cv.FILLED) #or -1
# cv.imshow('rect',blank)


#draw a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,0,255),thickness=-1)
# cv.imshow('circle',blank)


#draw a line

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,250),thickness=3)
# cv.imshow('line',blank)


#write text

cv.putText(blank,'Hello OpenCV',(150,150),cv.FONT_HERSHEY_DUPLEX,1.0,(255,0,255),thickness=3)

cv.imshow('Text',blank)

cv.waitKey(0)