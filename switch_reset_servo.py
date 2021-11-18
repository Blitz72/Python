from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

start_angle = 90
reset_angle = 0
 
def reset(start_angle, reset_angle, delay):
    '''Reset a Cync switch using a servo!  What could go wrong!

    reset(start_angle, reset_angle, delay):

    start_angle = the angle to return the servo to after the reset delay (integer 0 - 180)
    reset_angle = the angle to drive the servo to when "pressing" the switch button (integer 0 - 180)
    delay = the time in seconds to hold the switch button
    '''

    start_time = time.time()
    print(start_time)
    kit.servo[0].angle = reset_angle
    timed_out = False
    while not timed_out:
        timed_out = time.time() - start_time > delay
    if timed_out:
        kit.servo[0].angle = start_angle
    time.sleep(1)


reset(start_angle, reset_angle, 13)
