#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
#ev3 = EV3Brick
belt_motor = Motor(Port.D)
feed_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)
while True:
    print("reseting motors")
    feed_motor.run_until_stalled(120, duty_limit=50)
    feed_motor.run_angle(450, -200)
    
    belt_motor.run(-500)
    while not touch_sensor.pressed():
        pass
    belt_motor.stop()
    wait(1000)
    belt_motor.reset_angle(0)
    color_list = []
    
    while len(color_list) <= 8:
        if len(color_list) < 8:
            #ev3.screen.load_image(ImageFile.Right)
            #ev3.screen.print(len(color_list))
            print("Inside the color list loop")

            while True:
                color = color_sensor.color()    
                if color in POSSIBLE_COLORS:
                    print("Scan Color")
                    print(color)
                    wait(2000)
                    break      
            #ev3.speaker.beep(1000, 100)
            print("Finished Scanning")
            color_list.append(color)
            print("added color to color_list")
            
            print("Current List: ")
            for color in color_list:
                print(color)
        if len(color_list) == 8:
            for color in color_list:
                if color == Color.GREEN:
                    #ev3.speaker.say('green')
                    
                    print("Belt Motor Green")
                    wait(1500)
                    feed_motor.run_angle(1500, 200)
                    feed_motor.run_angle(1500, -200)
                   
                elif color == Color.YELLOW:
                    #ev3.speaker.say('yellow')
                    belt_motor.run_angle(500, 240)
                    print("Belt Motor Yellow")
                    wait(1500)
                    feed_motor.run_angle(1500, 180)
                    feed_motor.run_angle(1500, -180)
                    belt_motor.run(-500)
                    while not touch_sensor.pressed():
                        pass
                    belt_motor.stop()
                    wait(1000)
                    belt_motor.reset_angle(0)
                
                elif color == Color.RED:
                    #ev3.speaker.say('red')
                    belt_motor.run_angle(500, 460)
                    print("Belt Motor Red")
                    wait(1500)
                    feed_motor.run_angle(1500, 180)
                    feed_motor.run_angle(1500, -180)
                    belt_motor.run(-500)
                    while not touch_sensor.pressed():
                        pass
                    belt_motor.stop()
                    wait(1000)
                    belt_motor.reset_angle(0)
                    

                
                        

                    