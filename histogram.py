import cv2 as cv
from read import rescaleFrame   
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('images/scene.webp')
img=rescaleFrame(img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

blank=np.zeros(img.shape[:2],dtype='uint8')

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)


masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)

#Grayscale Histogram

# gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# no.of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


#Color Histogram

color=('b','g','r')

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# no.of pixels')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)

