# In dieser Datei können eigene Funktionen definiert werden. Es können auch weitere Dateien angelegt werden, die dann in main.py importiert werden müssen

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color, Stop
from pybricks.tools import wait, StopWatch, DataLog

def calibrate_ultrasonic(head_motor, ultrasonic_sensor):
    # Turn the head in such way that the distance becomes as small as possible between the ultrasonic sensor and the wall.
    max_rotation_angle = 160      # Maximum angle to rotate the head
    buffer_size = 10               # Number of measurements to confirm the minimum
    speed = 150                   # Rotation speed in degrees per second
    confirmation_counter = 0      # Counter for confirmation buffer

    measurements = []
    head_motor.reset_angle(0)     # Reset motor angle to zero
    head_motor.run(speed)

    min_distance = float('inf')
    min_angle = 0

    while head_motor.angle() < max_rotation_angle:
        current_angle = head_motor.angle()
        current_distance = ultrasonic_sensor.distance()
        measurements.append((current_angle, current_distance))
        print("Angle: {:.2f}°, Distance: {:.2f} mm".format(current_angle, current_distance))
        if current_distance < min_distance:
            min_distance = current_distance
            min_angle = current_angle
            confirmation_counter = buffer_size
            print("New minimum distance found: {:.2f} at angle {:.2f}".format(min_distance, min_angle))
        elif current_distance > min_distance and confirmation_counter > 0:
            confirmation_counter -= 1
            print("Confirmation buffer: {} remaining".format(confirmation_counter))
            if confirmation_counter == 0:
                print("Minimum distance confirmed.")
                head_motor.hold()
                break

        wait(10)

    rotation_needed = min_angle - head_motor.angle()
    print("Rotating back to minimum angle: {:.2f} degrees".format(min_angle))
    head_motor.run_angle(speed=150, rotation_angle=rotation_needed, then=Stop.BRAKE)

    print("Calibration complete. Minimum distance: {:.2f} at angle {:.2f}".format(min_distance, min_angle))