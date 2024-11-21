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
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)
head_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S2)
gyro_sensor = GyroSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S3)

calibrate_ultrasonic(head_motor,ultrasonic_sensor)

while touch_sensor.pressed() == False:
    wait(1)

go_to_start_position(left_motor, right_motor, ultrasonic_sensor, color_sensor, head_motor)

while True:
    distances = measure_3_distances(head_motor, ultrasonic_sensor)
    maximum_distance = max(distances, key=distances.get)
    if maximum_distance == "right":
        turn_base(left_motor, right_motor, gyro_sensor, degrees=90)
    elif maximum_distance == "left":
        turn_base(left_motor, right_motor, gyro_sensor, degrees=-90)

    finished = motors_on(left_motor, right_motor, ultrasonic_sensor, color_sensor)
    if finished:
        break

print("End reached.")
ev3.screen.load_image(Image(ImageFile.THUMBS_UP))
ev3.light.off()

################# music

# ev3.speaker.set_volume(100)

# party_gewinn_melodie = [
#     # Abschnitt 1: "Yeah! Wir haben gewonnen"
#     'C4/8', 'E4/8', 'G4/4', 'C5/8', 'G4/8', 'E4/4', 'C4/2',
    
#     # Abschnitt 2: "Feiern wir die Nacht"
#     'D4/8', 'F4/8', 'A4/4', 'D5/8', 'A4/8', 'F4/4', 'D4/2',
    
#     # Abschnitt 3: "Freude und Spaß"
#     'E4/8', 'G4/8', 'B4/4', 'E5/8', 'B4/8', 'G4/4', 'E4/2',
    
#     # Abschnitt 4: "Gemeinsam sind wir stark"
#     'F4/8', 'A4/8', 'C5/4', 'F5/8', 'C5/8', 'A4/4', 'F4/2',
    
# ]
# ev3.speaker.play_notes(party_gewinn_melodie, tempo=200)
