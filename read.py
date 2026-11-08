import cv2 as cv

#Reading the images

# img=cv.imread('images/me.png')

# cv.imshow('Myself',img)


#rescale the frames

def rescaleFrame(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)




#Reading the videos
capture=cv.VideoCapture('videos/v1.mp4')

# while True:
#     isTrue,frame=capture.read()
#     frame_rescaled=rescaleFrame(frame)
#     cv.imshow('video',frame)
#     cv.imshow('video2',frame_rescaled)
    
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()





img=cv.imread('images/me.png')


# cv.imshow('Myself',img)

img_resize=rescaleFrame(img)

# cv.imshow('Myself2',img_resize)

cv.waitKey(0)