import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_profileface.xml')


    
def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    faces1 = face_cascade1.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    profile = profile_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
   
    detected = False
    
    roi_gray = np.zeros((100,100))
    if(len(faces))!=0:
        detected = True
        for (x,y,w,h) in faces:
            #print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (255,0,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            return roi_gray,detected
            #cv2.rectangle(gray, (x,y), (end_cord_x,end_cord_y),color,stroke)
    elif(len(faces1))!=0:
        detected = True
        for (x,y,w,h) in faces1:
            #print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (255,0,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            return roi_gray,detected
       
            #cv2.rectangle(gray, (x,y), (end_cord_x,end_cord_y),color,stroke)        
    elif(len(profile))!=0:
       detected = True
       for (x,y,w,h) in profile:
            #print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (0,255,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            return roi_gray,detected
            #cv2.rectangle(gray, (x,y), (end_cord_x,end_cord_y),color,stroke)"""  
    else: 
        return None,detected