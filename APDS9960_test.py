from board import SCL, SDA
import busio
from adafruit_apds9960.apds9960 import APDS9960
import subprocess
import json
from time import sleep

i2c = busio.I2C(SCL, SDA)

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
apds.gesture_gain = 3
apds.gesture_proximity_threshold = 1


# CPB Switch MAC
MAC_ADDRESS = '30:c0:1b:28:f3:12'
# C-Sleep MAC
#MAC_ADDRESS = 'a4:c1:38:4e:d7:40'
MESH_NAME = 'D72800380264'
MESH_PASS = '750469'


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
    while not success and attempts <= 3:
        results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
        success, results_list = check_success(results)
        attempts += 1
        sleep(0.5)
    return {'success': success, 'data': None}


while True:
    gesture = apds.gesture()
    if gesture == 0x01:
        print("up")
        set_power(MAC_ADDRESS, 'on', MESH_NAME, MESH_PASS)
    elif gesture == 0x02:
        print("down")
        set_power(MAC_ADDRESS, 'off', MESH_NAME, MESH_PASS)
    elif gesture == 0x03:
        print("left")
        set_power(MAC_ADDRESS, 'off', MESH_NAME, MESH_PASS)
    elif gesture == 0x04:
        print("right")
        set_power(MAC_ADDRESS, 'on', MESH_NAME, MESH_PASS)
