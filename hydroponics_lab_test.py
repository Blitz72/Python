#!/usr/bin/python3

import time

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

    time.sleep(DELAY_RUN_MODE)
