from controller import Robot,Camera,DistanceSensor,Speaker

robot = Robot()

timestep = int(robot.getBasicTimeStep())


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

def forward():
    motor1.setPosition(float("inf"))
    motor2.setPosition(float("inf"))
    motor3.setPosition(float("inf"))
    motor4.setPosition(float("inf"))
    motor1.setVelocity(10)
    motor2.setVelocity(10)
    motor3.setVelocity(10)
    motor4.setVelocity(10)
    
def turnLeft():
    stop()
    motor1.setPosition(float("inf"))
    motor2.setPosition(float("inf"))
    motor3.setPosition(float("inf"))
    motor4.setPosition(float("inf"))
    motor1.setVelocity(-10)
    motor2.setVelocity(10)
    motor3.setVelocity(-10)
    motor4.setVelocity(10) 
    
def turnRight():
    stop()
    motor1.setPosition(float("inf"))
    motor2.setPosition(float("inf"))
    motor3.setPosition(float("inf"))
    motor4.setPosition(float("inf"))
    motor1.setVelocity(10)
    motor2.setVelocity(-10)
    motor3.setVelocity(10)
    motor4.setVelocity(-10)        

def stop():
    motor1.setVelocity(0)
    motor2.setVelocity(0)
    motor3.setVelocity(0)
    motor4.setVelocity(0) 
    
def backward():
    motor1.setPosition(float("inf"))
    motor2.setPosition(float("inf"))
    motor3.setPosition(float("inf"))
    motor4.setPosition(float("inf"))
    motor1.setVelocity(-10)
    motor2.setVelocity(-10)
    motor3.setVelocity(-10)
    motor4.setVelocity(-10)  