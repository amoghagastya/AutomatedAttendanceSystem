# Face Recognition

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainner.yml')

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        cv2.imwrite('anish1.jpg',roi_gray)
        
        id_, conf = recognizer.predict(roi_gray)

        if conf>=45 and conf<=85:
           print(id_)
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),0)
        cv2.imshow('frame',frame)
        
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()    