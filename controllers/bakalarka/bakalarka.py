"""bakalarka controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Camera
import cv2
import numpy as np
import detection

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
camera = robot.getDevice("camera")
camera.enable(timestep)


motor1 = robot.getDevice("motor1")
motor2 = robot.getDevice("motor2")
motor3 = robot.getDevice("motor3")
motor4 = robot.getDevice("motor4")

motor1.setPosition(float("inf"))
motor2.setPosition(float("inf"))
motor3.setPosition(float("inf"))
motor4.setPosition(float("inf"))

motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
motor3.setVelocity(0.0)
motor4.setVelocity(0.0)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_profileface.xml')

time = 0
def forward():
    motor1.setVelocity(10)
    motor2.setVelocity(10)
    motor3.setVelocity(10)
    motor4.setVelocity(10)

def stop():
    motor1.setVelocity(0)
    motor2.setVelocity(0)
    motor3.setVelocity(0)
    motor4.setVelocity(0)    
    
    
while robot.step(timestep) != -1:
    detection.kokot()
    
    frame = np.array(camera.getImageArray(),dtype = 'uint8')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    faces1 = face_cascade1.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    profile = profile_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors=5)
    
    roi_gray = np.zeros((500,500))
    
    detected = False
    
    if(len(faces))!=0:
        detected = True
        for (x,y,w,h) in faces:
            print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (255,0,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y),color,stroke)
    if(len(faces1))!=0:
        detected = True
        for (x,y,w,h) in faces1:
            print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (255,0,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            cv2.rectangle(gray, (x,y), (end_cord_x,end_cord_y),color,stroke)        
    if(len(profile))!=0:
       detected = True
       for (x,y,w,h) in profile:
            print(x,y,w,h)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y+h,x:x+w]
            img_item ="my-image.png"
            cv2.imwrite(img_item, roi_gray)
            color = (0,255,0) #BGR
            stroke = 2
            end_cord_x= x+w
            end_cord_y= y+ h
            cv2.rectangle(gray, (x,y), (end_cord_x,end_cord_y),color,stroke)    
    cv2.imshow('frame',roi_gray)
    if detected == True:
        motor1.setPosition(10*3.14)
        motor2.setPosition(10*3.14)
        motor3.setPosition(10*3.14)
        motor4.setPosition(10*3.14)
        forward() 
    else:
        motor1.setPosition(float("inf"))
        motor2.setPosition(float("inf"))
        motor3.setPosition(float("inf"))
        motor4.setPosition(float("inf"))

        forward()
           
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break
    time+=1    

cap.release()
cv2.destroyAllWindows()