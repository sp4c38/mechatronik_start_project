#!/usr/bin/env pybricks-micropython
# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
import sys

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

from funktionen import *

# Hier wird die angeschlossene Hardware definiert und konfiguriert
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
head_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S1)
gyro_sensor = GyroSensor(Port.S4)
touch_sensor = TouchSensor(Port.S2)
ultrasonic_sensor = UltrasonicSensor(Port.S3)

# TODO: Later add gyroscope motor and gyroscope

ev3.light.on(Color.GREEN)
ev3.screen.load_image(Image(ImageFile.EV3)) # ImageFile.Neutral

maze = []

# head_motor.run_angle(300, 90)

# gyro_sensor.reset_angle(0)
# left_motor.run(40)
# right_motor.run(-40)
# while True:
#     angle = gyro_sensor.angle()
#     print("Current angle is", str(angle) + "°.")
#     if angle <= -90:
#         left_motor.brake()
#         right_motor.brake()
#         break
#     wait(1)
# ev3.screen.load_image(Image(ImageFile.THUMBS_UP))
# wait(1000)

while True:
    # print(ultrasonic_sensor.distance())
    # if color_sensor.color() == Color.BLACK: # Reached the end if black is detected.
    # if touch_sensor.pressed() == True:
    #     print("End reached.")
    #     ev3.screen.load_image(Image(ImageFile.THUMBS_UP))
    #     ev3.light.off()
    #     sys.exit(0)
    wait(200)