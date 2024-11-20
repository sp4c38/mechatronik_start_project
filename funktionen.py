# In dieser Datei können eigene Funktionen definiert werden. Es können auch weitere Dateien angelegt werden, die dann in main.py importiert werden müssen

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Color, Stop
from pybricks.tools import wait, StopWatch, DataLog

def measure_3_distances(head_motor, ultrasonic_sensor):
    distances = {"right": None, "front": None, "left": None}
    distances["left"] = ultrasonic_sensor.distance()
    turn_head(head_motor, degrees=90)
    distances["front"] = ultrasonic_sensor.distance()
    turn_head(head_motor, degrees=90)
    distances["right"] = ultrasonic_sensor.distance()
    print("Distances are {}.".format(distances))
    turn_head(head_motor, degrees=-90, wait=False)
    return distances

def turn_base(left_motor, right_motor, gyro_sensor, speed=300, degrees=90, adjustment_turn=False):
    """
    First make a quick 90° turn which will result in an actual turn of something like 105°.
    Then make a slow turn to correct for the misalignment. The slow turn is relatively accurat because the robot doesn't have that much momentum.
    """
    print("Turning {}°.".format(degrees))
    gyro_sensor.reset_angle(0)
    turn_clockwise = degrees > 0
    if turn_clockwise:
        # Turn clockwise
        left_motor.run(speed) #40)
        right_motor.run(-speed) #-20)
    else:
        # Turn anticlockwise
        left_motor.run(-speed) #-40)
        right_motor.run(speed) #20)
    
    while True:
        angle = gyro_sensor.angle()
        # print("Current angle is {}°.".format(str(angle)))
        if abs(angle) >= abs(degrees):
            left_motor.hold()
            right_motor.hold()
            break
        
        wait(1)

    wait(200)
    if not adjustment_turn:
        adjustment = abs(gyro_sensor.angle()) - abs(degrees)
        print("Adjusting turn by {}°.".format(adjustment))
        if turn_clockwise:
            adjustment *= -1
        turn_base(left_motor, right_motor, gyro_sensor, speed=40, degrees=adjustment, adjustment_turn=True)

def motors_on(left_motor, right_motor, ultrasonic_sensor):
    left_motor.run(-150)
    right_motor.run(-150)
    r = 0
    while(True):
        distance = ultrasonic_sensor.distance()
        stop =  distance - 40
        if stop <= 0:
            print("Stopped because distance is {}.".format(distance))
            break
        wait(50)
    left_motor.hold()
    right_motor.hold()
    

def turn_head(head_motor, degrees=90, wait=True):
    head_motor.run_angle(150, rotation_angle=degrees, wait=wait)

def turn_base(left_motor,right_motor,gyro_sensor,degrees=90,Clockwise=True):
    if Clockwise == True:
        left_motor.run(40)
        right_motor.run(-20)
    if Clockwise == False:
        left_motor.run(-40)
        right_motor.run(20)
    while True :
        angle = gyro_sensor.angle()
        print("Current angle is", str(angle) + "°.")
        if Clockwise == True:
            if angle <= -degrees:
                left_motor.brake()
                right_motor.brake()
                # break
        else:
            if angle >= degrees:
                left_motor.brake()
                right_motor.brake()
                # break
        wait(1)





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