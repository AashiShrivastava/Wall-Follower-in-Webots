# Maze Solving Logic : Follow the Wall

from controller import Robot

def start(robot):  
    # get the time step of the current world.
    timestep = 32
    max_speed=6.28

    # Enabling Motors
    left_motor=robot.getDevice("left wheel motor")
    right_motor=robot.getDevice("right wheel motor")
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0)
    
    # Enabling Proximity Sensor
    proximity_sensor=[]
    for i in range(8):
        sensor_name='ps'+str(i)
        proximity_sensor.append(robot.getDevice(sensor_name)) 
        proximity_sensor[i].enable(timestep)  
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        left_wall = proximity_sensor[5].getValue() > 80
        left_corner = proximity_sensor[6].getValue() > 80
        front_wall = proximity_sensor[7].getValue() > 80
        
        left_speed = max_speed
        right_speed = max_speed
        
        # Process sensor data here.        
        if front_wall:
            # Turn Right
            left_speed = max_speed
            right_speed = -max_speed
        
        else:
            if left_wall:
                # Drive Forward
                left_speed = max_speed
                right_speed = max_speed
                
            elif left_corner:
                # Drive Right
                left_speed = max_speed
                right_speed = max_speed/4 
                
            else: 
                # Turn Left
                left_speed = max_speed/4
                right_speed = max_speed            
    
        # Enter here functions to send actuator commands:
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
if __name__ == "__main__":
    # create the Robot instance.
    myBot=Robot()
    start(myBot)
    