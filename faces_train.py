import cv2 as cv
import numpy as np
import os


people=['Allu Arjun','Ana de Armas','Chris Hemsworth','Rajnikanth','Sabrina Carpenter']
DIR=r'C:\SaiChaithanya\OpenCV\images\faces\train'

features=[]
labels=[]
haar_cascade=cv.CascadeClassifier('frontal_face.xml')

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                # face_roi=cv.resize(face_roi,(200,200))
                features.append(face_roi)
                labels.append(label)

create_train()
print(f"Length of the features:{len(features)}")
print(f"Length of the labels:{len(labels)}")
print('Traning ...........')

features=np.array(features,dtype='object')
labels=np.array(labels)

#Now Train the features list and labels list
face_reconginzor=cv.face.LBPHFaceRecognizer_create(radius=2, neighbors=10, grid_x=10, grid_y=10)

face_reconginzor.train(features,labels)
face_reconginzor.save('face_trained.yml')


np.save('features.npy',features)
np.save('labels.npy',labels)
