#!/usr/bin/python3

import board
import busio
import subprocess
import json
import logging

from SMTP_test import Emailer

import adafruit_ads1x15.ads1015 as ADS

import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn
import time
import datetime as mytime

time.sleep(30)

# Create and configure log
LOG_FORMAT = '%(levelname)s: %(asctime)s --> %(message)s'
logging.basicConfig(filename = '/home/pi/Hydroponics_Lab/HP_LAB_LOG.txt', level=logging.DEBUG, format = LOG_FORMAT)
log = logging.getLogger()


# Setup Adafruit ADS1015 Analog to Digital Converter
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)

# GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)

# MAC address and credentials of test C by GE Full Color bulb
MAC_ADDRESS = 'f4:bc:da:3a:ae:a6'
MESHNAME = 'EF7CB2B03EE2'  #'D72800380264' = QA Lab
MESHPASS = '176962'  #'750469'       = QA Lab

DELAY_RUN_MODE = 300   # seconds
DELAY_FILL_MODE = 1  # seconds
FILL_TIMER_MAX = 400  # seconds

# fill_mode_flag = False
fill_mode_error = False
is_light_on = False
is_light_red = False
last_red_level = 50
email_sent_on_disconnect = False
LOW_LIMIT = 1.85   # VDC  2.045 VDC ~ 5 in.
FILL_LIMIT = 2.5   # VDC  2.530 VDC ~ 11 in.
#FILL_LIMIT = 2.2   # VDC  2.530 VDC ~ 11 in.
MID_LEVEL = (FILL_LIMIT + LOW_LIMIT)/2
SENSOR_MIN = 1.5  # VDC
OFFSET = 0.2      # VDC

# hours of operation for ./ble-backend in 24-hour format
HOURS_MIN = 7
HOURS_MAX = 21

ads.gain = 1
# ads.mode = 0
# print(ads.mode)

# define ADS channel
chan = AnalogIn(ads, ADS.P0)


########################################################### FUNCTIONS ##############################################################

def check_success(results):

    success = False
    results_list = []
    for line in results.stdout.readlines():
        decoded_line = line.decode('utf-8')
        results_list.append(decoded_line[0:-1])
        print(decoded_line)
    for l in results_list:
        if 'Generated' in l:
            success = True
    print('RESULTS LIST: ', results_list)
    return success, results_list


def set_power(mac, on_or_off, meshname, meshpass):

    results_list = []
    attempts = 0
    success = False
    print('Setting power on/off at:', time.asctime(time.localtime()))
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
        else:
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
        success, results = check_success(results)
        attempts += 1
        time.sleep(0.5)
    return {'success': success, 'data': None}


def set_rgb(mac, rVal, gVal, bVal, meshname, meshpass):

    results_list = []
    attempts = 0
    success = False
    print('Setting RGB at:', time.asctime(time.localtime()))
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command=rgb', f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
        else:
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command=rgb', f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
        success, results = check_success(results)
        attempts += 1
        time.sleep(0.5)
    return {'success': success, 'data': None}


def identify(mac, meshname, meshpass):

    results_list = []
    attempts = 0
    success = False
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command=stopIndicate'], stdout=subprocess.PIPE)
        success, results = check_success(results)
        attempts += 1
        time.sleep(0.5)
    return {'success': success, 'data': None}


def ping_network():
    network_ip = '192.168.1.254'
    success = False
    results = subprocess.Popen(['ping', '-c1', f'{network_ip}'], stdout=subprocess.PIPE)
    results_list = []
    for line in results.stdout.readlines():
        decoded_line = line.decode('utf-8')
        results_list.append(decoded_line[0:-1])
        print(decoded_line)
    for line in results_list:
        if '1 received' in line:
            success = True
    return success


def restart_wifi():
    success = False
    subprocess.Popen(['sudo', 'systemctl', 'daemon-reload'], stdout=subprocess.PIPE)
    time.sleep(2)
    results = subprocess.Popen(['sudo', 'systemctl', 'restart', 'dhcpcd'], stdout=subprocess.PIPE)
#     results_list = []
#     for line in results.stdout.readlines():
#         decoded_line = line.decode('utf-8')
#         results_list.append(decoded_line[0:-1])
#         print(decoded_line)


def sensor_error():
    
    global email_sent_on_disconnect, light_enable, is_light_on, is_light_red
    
    # This line is for debug purposes.  Comment out for production
#     email_sent_on_disconnect = True
    
    # turn off solenoid ASAP!
    GPIO.output(4, GPIO.LOW)
    
    print('Sensor disconnected!')
    if not ping_network():
        restart_wifi()
        time.sleep(20)
    print('is_light_red: ', is_light_red)
    # turn bulb red
    if light_enable:
        if not is_light_on:
            if set_power(MAC_ADDRESS, 'on', MESHNAME, MESHPASS)['success']:
                is_light_on = True
                print('Good morning! Turning light on!')
                if not is_light_red:
                    if set_rgb(MAC_ADDRESS, 50, 0, 0, MESHNAME, MESHPASS)['success']:
                        is_light_red = True
        else:
            print('Light is already on!')
            if not is_light_red:
                if set_rgb(MAC_ADDRESS, 50, 0, 0, MESHNAME, MESHPASS)['success']:
                    is_light_red = True
    else:
        if is_light_on:
            if set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)['success']:
                is_light_on = False
                print('Nighty night!  Turning light off!')
        else:
            print('Light is already off!')
            
    try:
        if not email_sent_on_disconnect:
            log.warning('Sensor disconnected!')
            sender = Emailer()
            # add in multiple contacts as comma separated strings: sendTo = ['david.bauer2@ge.com', 'mathew.sommers@ge.com']
            sendTo = ['mathew.sommers@ge.com','jasommerscle@gmail.com']
#             sendTo = ['mathew.sommers@ge.com']
#             sendTo = ['david.bauer2@ge.com']
            emailSubject = 'Hydroponics Reservoir Sensor Alert!'
            emailContent = 'The water level sensor is disconnected!'
            if sender.sendmail(sendTo, emailSubject, emailContent) == None:
                email_sent_on_disconnect = True

    except Exception as e:
        print('Error: ', e)
        

def fill_reservoir():
    
    global fill_mode_error, light_enable, is_light_on
    if light_enable:
        if not is_light_on:
            if set_power(MAC_ADDRESS, 'on', MESHNAME, MESHPASS)['success']:
                is_light_on = True
                print('Good morning! Turning light on!')
                if set_rgb(MAC_ADDRESS, 0, 0, 50, MESHNAME, MESHPASS)['success']:
                    is_light_red = False
        else:
            if set_rgb(MAC_ADDRESS, 0, 0, 50, MESHNAME, MESHPASS)['success']:
                is_light_red = False
    # set timer start value
    start_time = time.time()
    # open fill solenoid
    GPIO.output(4, GPIO.HIGH)
    while chan.voltage < FILL_LIMIT:
        if chan.voltage < SENSOR_MIN:
            sensor_error()
            break
        print(chan.voltage)
        time.sleep(DELAY_FILL_MODE)
        print('Fill Timer: ', int(time.time() - start_time))
#         print('fill_mode_error: ', fill_mode_error)
        if time.time() - start_time > FILL_TIMER_MAX:
            fill_mode_error = True
            if set_rgb(MAC_ADDRESS, 50, 0, 0, MESHNAME, MESHPASS)['success']:
                is_light_red = True
            break
    end_time = time.time()
    fill_time = end_time - start_time
    print('fill_time: ', fill_time)
    GPIO.output(4, GPIO.LOW)
    asctime_start = time.asctime(time.localtime(start_time))
    fill_time2string = '{0:.2f}'.format(fill_time)
    if not ping_network():
        restart_wifi()
        time.sleep(20)
    try:
        log.info('Reservoir refilled. Process time: ' + fill_time2string)
        sender = Emailer()
        # add in multiple contacts as comma separated strings: sendTo = ['david.bauer2@ge.com', 'mathew.sommers@ge.com']
        sendTo = ['mathew.sommers@ge.com','jasommerscle@gmail.com']
#         sendTo = ['mathew.sommers@ge.com']
#        sendTo = ['david.bauer2@ge.com']
        emailSubject = 'Hydroponics Reservoir Refill Alert!'
        emailContent = 'The hydroponics reservoir has been refilled.  <br> The process began on ' + asctime_start + ' and took ' + fill_time2string + ' seconds to complete!  <br>-The Tower Garden Robot'
        sender.sendmail(sendTo, emailSubject, emailContent)
    except Exception as e:
        print('Error: ', e)
#     fill_mode_flag = False
    return


######################################################### PROGRAM START ############################################################


# initialize solenoid to closed/off
GPIO.output(4, GPIO.LOW)

# Tell log file we've started (again)
log.info('Hydroponics.py running...')

# test ./ble-backend
if set_power(MAC_ADDRESS, 'on', MESHNAME, MESHPASS)['success']:
    is_light_on = True
set_rgb(MAC_ADDRESS, 15, 0, 30, MESHNAME, MESHPASS)


time.sleep(5)

#light_turned_off = False

# 8.0 inches = ~2.20 volts
# 0.0 inches = ~1.65 volts

while True:

    # check time, enable ./ble-backend between HOURS_MIN and HOURS_MAX
    if HOURS_MIN <= time.localtime()[3] < HOURS_MAX:
    #if HOURS_MIN <= mytime.datetime.now().hour < HOURS_MAX:
        light_enable = True
        current_time = time.localtime()
    else:
        light_enable = False

    print(chan.value, chan.voltage)

    if not fill_mode_error:
        if chan.voltage > SENSOR_MIN:
            email_sent_on_disconnect = False
            if chan.voltage < LOW_LIMIT:
                print('LOW WATER LEVEL!')
                fill_reservoir()
            elif chan.voltage >= LOW_LIMIT:
                if chan.voltage >= LOW_LIMIT:
                    print('Water level OK!')
                red_level = int((MID_LEVEL - (chan.voltage))*50/(MID_LEVEL - LOW_LIMIT))
                if red_level < 0:
                    red_level = 0
                elif red_level > 50:
                    red_level = 50
                print('red_level: ', red_level)
                if light_enable:
                    if not is_light_on:
                        if set_power(MAC_ADDRESS, 'on', MESHNAME, MESHPASS)['success']:
                            is_light_on = True
                            print('Good morning! Turning light on!')
                    print('Attempting to set red level to: ', red_level)
                    if red_level != last_red_level:
                        if set_rgb(MAC_ADDRESS, red_level, 50, 0, MESHNAME, MESHPASS)['success']:
                            is_light_red = False
                            last_red_level = red_level
                else:  # we are outside of business hours
                    if is_light_on:
                        if set_power(MAC_ADDRESS, 'off', MESHNAME, MESHPASS)['success']:
                            is_light_on = False
                            print('Nighty night! Turning light off!')
                GPIO.output(4, GPIO.LOW)
        else:
            sensor_error()

    time.sleep(DELAY_RUN_MODE)

    if fill_mode_error and chan.voltage > LOW_LIMIT + OFFSET:
        fill_mode_error = False
#     print('fill_mode_error: ', fill_mode_error)
