import cv2 as cv
import read

img=cv.imread('images/group2.jpg')
# img=read.rescaleFrame(img)
# cv.imshow('Face',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

haar_cascade=cv.CascadeClassifier('frontal_face.xml')
face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
print(f"No. of Faces are {len(face_rect)}")

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)     

cv.imshow('Detected Faces',img)

cv.waitKey(0)