# In dieser Datei können eigene Funktionen definiert werden. Es können auch weitere Dateien angelegt werden, die dann in main.py importiert werden müssen

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color
from pybricks.tools import wait, StopWatch, DataLog

# def calibrate_ultrasonic(head_motor, ultrasonic_sensor):
#     while ultrasonic_sensor():
#         head_motor.run_angle(150,360)
#         distance = ultrasonic_sensor.distance()
#         print(distance)
#         for x in head_motor.run_angle():
#             min_distance
#             min_distance = min_distance < distance
        
def motors_on(left_motor,right_motor,ultrasonic_sensor):
    left_motor.run(-150)
    right_motor.run(-150)
    while(True):
        distance = ultrasonic_sensor.distance()
        stop =  distance - 60
        if stop<=0 :
            break
        wait(0.1)
    left_motor.brake()
    right_motor.brake()
    






    