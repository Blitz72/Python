#!/usr/bin/python3

# import board
# import busio
# import subprocess
# import json

# import adafruit_ads1x15.ads1015 as ADS

# import RPi.GPIO as GPIO
# from adafruit_ads1x15.analog_in import AnalogIn
import time

# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1015(i2c)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(4, GPIO.OUT)

# MAC address and credentials of test C by GE Full Color bulb
MAC_ADDRESS = 'f4:bc:da:3a:ae:a6'
MESHNAME = ''  #'D72800380264' = QA Lab
MESHPASS = ''  #'750469'       = QA Lab

DELAY_RUN_MODE = 10   # seconds
DELAY_FILL_MODE = 1  # seconds
FILL_TIMER_MAX = 300  # seconds

# fill_mode_flag = False
fill_mode_error = False
LOW_LIMIT = 2.045   # VDC  2.045 VDC ~ 5 in.
FILL_LIMIT = 2.53   # VDC  2.530 VDC ~ 11 in.
MID_LEVEL = (FILL_LIMIT + LOW_LIMIT)/2
SENSOR_MIN = 1.5  # VDC
OFFSET = 0.2      # VDC

# hours of operation for ./ble-backend in 24-hour format
HOURS_MIN = 7
HOURS_MAX = 14

# ads.gain = 1
# ads.mode = 0
# print(ads.mode)

# define ADS channel
# chan = AnalogIn(ads, ADS.P0)


# def sensor_error():

#     print('Sensor disconnected!')
#     GPIO.output(4, GPIO.LOW)
#     # turn bulb red
#     set_rgb(MAC_ADDRESS, 50, 0, 0, MESHNAME, MESHPASS)


# def fill_reservoir():

#     set_rgb(MAC_ADDRESS, 0, 0, 50, MESHNAME, MESHPASS)
#     global fill_mode_error
#     # set timer start value
#     start_time = time.time()
#     # open fill solenoid
#     GPIO.output(4, GPIO.HIGH)
#     while chan.voltage < FILL_LIMIT:
#         if chan.voltage < SENSOR_MIN:
#             sensor_error()
#             break
#         print(chan.voltage)
#         time.sleep(DELAY_FILL_MODE)
#         print('Fill Timer: ', int(time.time() - start_time))
# #         print('fill_mode_error: ', fill_mode_error)
#         if time.time() - start_time > FILL_TIMER_MAX:
#             fill_mode_error = True
#             set_rgb(MAC_ADDRESS, 50, 0, 0, MESHNAME, MESHPASS)
#             break
#     GPIO.output(4, GPIO.LOW)
# #     fill_mode_flag = False
#     return


# def check_success(results):

#     success = False
#     results_list = []
#     for line in results.stdout.readlines():
#         decoded_line = line.decode('utf-8')
#         results_list.append(decoded_line[0:-1])
#         print(decoded_line)
#     for l in results_list:
#         if 'Generated' in l:
#             success = True
#     print('RESULTS LIST: ', results_list)
#     return success, results_list


# def set_power(mac, on_or_off, meshname, meshpass):

#     # results_list = []
#     attempts = 0
#     success = False
#     while not success and attempts < 3:
#         if meshname != '':
#             results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
#         else:
#             results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
#         success, results = check_success(results)
#         attempts += 1
#         time.sleep(0.5)
#     return {'success': success, 'data': None}


# def set_rgb(mac, rVal, gVal, bVal, meshname, meshpass):

#     # results_list = []
#     attempts = 0
#     success = False
#     while not success and attempts < 3:
#         if meshname != '':
#             results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command=rgb', f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
#         else:
#             results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command=rgb', 
# f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
#         success, results = check_success(results)
#         attempts += 1
#         time.sleep(0.5)
#     return {'success': success, 'data': None}


# initialize solenoid to closed/off
# GPIO.output(4, GPIO.LOW)

# test ./ble-backend
# set_power(MAC_ADDRESS, 'on', MESHNAME, MESHPASS)
# set_rgb(MAC_ADDRESS, 0, 0, 50, MESHNAME, MESHPASS)

# time.sleep(5)

# set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)

# time.sleep(1)

#light_turned_off = False

# 8.0 inches = ~2.20 volts
# 0.0 inches = ~1.65 volts

while True:

    # check time, enable ./ble-backend between HOURS_MIN and HOURS_MAX
    print('Time: ', time.localtime())
    print('Time (hours): ', time.localtime()[3])
    if HOURS_MIN <= time.localtime()[3] < HOURS_MAX:
        light_enable = True
#        light_enable_flag = True
#       light_turned_off = False
    else:
        light_enable = False
    print('light_enable: ', light_enable)

    # if light_enable is False:
    #     print('Turning light off!')
    #     set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)
#        light_enable_flag = False
#       light_turned_off = True

    # if chan.voltage <= SENSOR_MIN:
    #     sensor_error()
    # print(chan.value, chan.voltage)

    # if not fill_mode_error:
        # if SENSOR_MIN < chan.voltage < LOW_LIMIT:
        #     print('LOW WATER LEVEL!')
#             fill_mode_flag = True
            # if light_enable:
            #     set_rgb(MAC_ADDRESS, 50, 50, 0, MESHNAME, MESHPASS)
            # else:
            #     set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)
            # fill_reservoir()
        # elif chan.voltage >= LOW_LIMIT:
        #     print('Water level OK!')
        #     red_level = int((MID_LEVEL - (chan.voltage))*50/(MID_LEVEL - LOW_LIMIT))
        #     if red_level < 0:
        #         red_level = 0
        #     elif red_level > 50:
        #         red_level = 50
        #     print('red_level: ', red_level)
        #     if light_enable:
        #         set_rgb(MAC_ADDRESS, red_level, 50, 0, MESHNAME, MESHPASS)
        #     else:
        #         set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)
        #     GPIO.output(4, GPIO.LOW)

    time.sleep(DELAY_RUN_MODE)

    # if fill_mode_error and chan.voltage > LOW_LIMIT + OFFSET:
    #     fill_mode_error = False
#     print('fill_mode_error: ', fill_mode_error)