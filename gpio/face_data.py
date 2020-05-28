import numpy as np
import cv2
face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) #넓이 설정
cap.set(4,480) #높이 설정
face_id = input('\n enter user id end press <return> ==> ')
print("\n [INFO]Initializing face capture. Look the camera and wait...")
count = 0
while(True):
    ret,img = cap.read()
    img = cv2.flip(img,0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    # faces = faceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.2,
    #     minNeighbors=5,
        
    #     minSize=(20, 20)
    # )
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count +=1
        cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])

    cv2.imshow('image',img)
    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break
    elif count>=30:
        break
print("\n[INFO]EXIT")
cap.release()
cv2.destroyAllWindows()