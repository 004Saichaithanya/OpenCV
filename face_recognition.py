import cv2 as cv
import read
import numpy as np


haar_cascade=cv.CascadeClassifier('frontal_face.xml')
people=['Allu Arjun','Ana de Armas','Chris Hemsworth','Rajnikanth','Sabrina Carpenter']

face_reconginzor=cv.face.LBPHFaceRecognizer_create()
face_reconginzor.read('face_trained.yml')

# img=cv.imread(r'C:\SaiChaithanya\OpenCV\images\faces\val\Allu Arjun\images.jpg')
# img=cv.imread(r'C:\SaiChaithanya\OpenCV\images\faces\val\ana de armas\ana.jpg')
# img=cv.imread(r'C:\SaiChaithanya\OpenCV\images\faces\val\chris\chris1.jpg')
# img=read.rescaleFrame(img)
img=cv.imread(r'C:\SaiChaithanya\OpenCV\images\faces\val\Rajnikanth\rajinikanth201805301.jpg')
# img=read.rescaleFrame(img)
# img=cv.imread(r'C:\SaiChaithanya\OpenCV\images\faces\val\Sabrina\sabrina_carpenter_photo_shoot-t2.jpg')
img=read.rescaleFrame(img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+w]
    label,confidence=face_reconginzor.predict(face_roi)
    print(f"Label ={people[label]} of confidence {confidence}")
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected image',img)
cv.waitKey(0)