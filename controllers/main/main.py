"""bakalarka controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Camera,DistanceSensor,Speaker,Accelerometer

import cv2
import numpy as np
import detection
from skimage import color,transform
from keras import models
import tensorflow as tf
import time
import threading
import comunication
import asyncio



model = models.load_model("..\\..\\model\\male_female_28_28_1.h5")
model1 = models.load_model("..\\..\\model\\young_old_28_28_1.h5")

robot = Robot()

timestep = int(robot.getBasicTimeStep())
timestep = 1


camera = robot.getDevice("camera")
camera.enable(timestep)

ds1 = robot.getDevice("ds1")
ds1.enable(timestep)
ds2 = robot.getDevice("ds2")
ds2.enable(timestep)
ds3 = robot.getDevice("ds3")
ds3.enable(timestep)


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

speaker = robot.getDevice("speaker")
speaker.setEngine("microsoft")

current_velocity = 10

def forward():
    motor1.setVelocity(current_velocity)
    motor2.setVelocity(current_velocity)
    motor3.setVelocity(current_velocity)
    motor4.setVelocity(current_velocity)
    
def turnLeft():
    stop()
    motor1.setVelocity(0)
    motor2.setVelocity(current_velocity)
    motor3.setVelocity(0)
    motor4.setVelocity(current_velocity) 
    
def turnRight():
    stop()
    motor1.setVelocity(current_velocity)
    motor2.setVelocity(0)
    motor3.setVelocity(current_velocity)
    motor4.setVelocity(0)        

def stop():
    motor1.setVelocity(0)
    motor2.setVelocity(0)
    motor3.setVelocity(0)
    motor4.setVelocity(0) 
    
def backward():
    motor1.setVelocity(-current_velocity)
    motor2.setVelocity(-current_velocity)
    motor3.setVelocity(-current_velocity)
    motor4.setVelocity(-current_velocity)  
    
Person = False  
gender = "undetected"
lock = "unlocked"

motor1.setPosition(float("inf"))
motor2.setPosition(float("inf"))
motor3.setPosition(float("inf"))
motor4.setPosition(float("inf"))

counter_right = 0
counter_left = 0
interaction_state = False

while robot.step(timestep) != -1:
    distance1 = 0.7611*np.power(ds1.getValue(),-0.9313)-0.1252
    distance2 = 0.7611*np.power(ds2.getValue(),-0.9313)-0.1252
    distance3 = 0.7611*np.power(ds3.getValue(),-0.9313)-0.1252
    
    frame = np.array(camera.getImageArray(),dtype = 'uint8')
    img,detected = detection.detect(frame)
    
    if img is None:
        img = np.zeros((50,50))
    if detected ==True and Person ==False:
        
        #spracujeme obraz z kamery aby sme ho vedeli dat do CNN
        img = transform.resize(img,(28,28))
        img= tf.keras.utils.normalize(img,axis=1)
        cnn_input = img.reshape(-1, 28, 28, 1)
          
        #predikujem pohlavie a vek
        gender_prediction = model.predict(cnn_input)
        age_prediction = model1.predict(cnn_input)
        if  gender_prediction[0][0]> gender_prediction[0][1]:
            gender = "male"
        else:
            gender = "female" 
            
        if age_prediction[0][0]>age_prediction[0][1]:
            age = "young"
        else:
            age = "old" 
        lock = "locked"       
        print(gender)
        print(age) 
        Person =True  
    
    if detected ==True and interaction_state ==False:
        current_velocity = (motor1.getVelocity() + motor2.getVelocity()) /2
        if  motor1.getVelocity()>=0.05:
            motor1.setVelocity(current_velocity -0.05) 
            motor2.setVelocity(current_velocity -0.05) 
            motor3.setVelocity(current_velocity -0.05) 
            motor4.setVelocity(current_velocity -0.05)
    
    if distance2 >1.4 and distance3>1.4 and distance1>1.4 and interaction_state ==False:
        if counter_right >0:
            turnLeft()
            counter_right-=1
        elif counter_left >0:
            turnRight()
            counter_left-=1
        else:       
            forward()
            print("forward")
     
    elif distance1 < distance3 and distance1<1.4 and interaction_state ==False:
        counter_left = 0
        counter_right +=1
        turnRight()
        print("right")
    
    elif distance3 < distance1 and distance3<1.4 and interaction_state ==False:
        counter_right = 0
        counter_left +=1
        turnLeft()
        print("left")    
        
    elif distance2<1.4 and Person == False and interaction_state ==False:
        backward()
        print("backward") 
    
    elif distance2<1.4 and Person == True and interaction_state ==False: 
        stop()
        print("stop")
         
    else:
        pass         
   
    print(motor1.getVelocity(),motor2.getVelocity(),motor3.getVelocity(),motor4.getVelocity())    
    
    if (motor1.getVelocity()+motor2.getVelocity()+motor3.getVelocity()+motor4.getVelocity()<0.08) and Person == True and interaction_state ==False: 
        stop()
        break
                    
    cv2.imshow('frame',img)   
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break 


locker = True
interaction_state = True
print("QUIZ?")
path  = "..\\..\\jokes\\kids\\quiz.mp3"
def ask():
    speaker.playSound(speaker,speaker,path,1.0,1.0,0,False)
    speaker.stop(path)
    locked = False
    return locked
    
locked = ask()    
if locked == False:
    comunication.answer()


    




#time.sleep(10)

#print("bad thing")

 
#speaker.playSound(speaker,speaker,path,1.0,1.0,0,False)


#cap.release()
#cv2.destroyAllWindows()