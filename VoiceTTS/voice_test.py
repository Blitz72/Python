from Voice_agent import Voice_agent
from supported_colors import supported_colors_list
import random
import board
import busio
import adafruit_tsl2591
import adafruit_tcs34725
import adafruit_tca9548a
import subprocess
import json
from time import sleep


# source ./linear_regression/bin/activate
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

# Alexa Voice Service protocol (what I think the C by GE Skill maps to, at least)
#
#                                                         | slot |
#     Alexa,     set     <device_name>/<group_name>    to   red.
# | wake word | launch |      invocation name       | utterance (the intent of the command)


# voice agent name
voice_agent = 'alexa'  # 'alexa' or 'google'

dir_name = voice_agent.capitalize()
# print(dir_name)

# path to store generated voice files
path = f'/home/pi/Python/VoiceTTS/{dir_name}/voice_files/'

va = Voice_agent(voice_agent, path)

# print(board.SCL)
i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
# print(tca[0].tca.__dict__.values)

tcs = adafruit_tcs34725.TCS34725(tca[0])
tcs.integration_time = 100

tsl = adafruit_tsl2591.TSL2591(tca[1])
tsl.gain = adafruit_tsl2591.GAIN_LOW
tsl.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

# either single control with specific bulb name or group control
group_name = 'color bulb'  # 'color bulb' or 'office lights'

# Bluetooth MAC address
mac = 'f4:bc:da:34:1d:5f'
mesh_name = 'EF7CB2B03EE2'  #'D72800380264' = QA Lab
mesh_pass = '176962'  #'750469'       = QA Lab

def check_success_BLE(results):
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

def set_power_BLE(mac, on_or_off, meshname, meshpass):
    results_list = []
    attempts = 0
    success = False
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
        else:
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command={on_or_off}'], stdout=subprocess.PIPE)
        success, results = check_success_BLE(results)
        attempts += 1
        sleep(0.5)
    return {'success': success, 'data': None}

def set_rgb_BLE(mac, rVal, gVal, bVal, meshname, meshpass):
    results_list = []
    attempts = 0
    success = False
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command=rgb', f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
        else:
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command=rgb', f'-rVal={rVal}', f'-gVal={gVal}', f'-bVal={bVal}'], stdout=subprocess.PIPE)
        success, results = check_success_BLE(results)
        attempts += 1
        sleep(0.5)
    return {'success': success, 'data': None}

def set_cct_BLE(mac, cctVal, meshname, meshpass):
    results_list = []
    attempts = 0
    success = False
    while not success and attempts < 3:
        if meshname != '':
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-meshname={meshname}', f'-meshpass={meshpass}', f'-command=cct', f'-cctVal={cctVal}'], stdout=subprocess.PIPE)
        else:
            results = subprocess.Popen(['sudo', '/home/pi/ble-backend', f'-mac={mac}', f'-addr={mac}', f'-command=cct', f'-cctVal={cctVal}'], stdout=subprocess.PIPE)
        success, results = check_success_BLE(results)
        attempts += 1
        sleep(0.5)
    return {'success': success, 'data': None}

def set_power(group, value):
    emphasis_level = 'moderate'
    success = va.speak(f'turn <emphasis level="{emphasis_level}"> {value} </emphasis> the {group}, <break time="1s"/>')
    # print(success)
    return {'success': success, 'data': None}
    # sleep(15)

def set_brightness(group, value):
    if value == 'dim' or value == 'brighten':
        added_str = ''
        launch_word = value
        emphasis_level = 'moderate'
    else:
        added_str = f'to {value}%'
        launch_word = 'set'
        emphasis_level = 'none'
    success = va.speak(f'<emphasis level="{emphasis_level}"> {launch_word} </emphasis> the {group} {added_str}, <break time="1s"/>')
    # print(success)
    return {'success': success, 'data': None}
    # sleep(15)

def set_color(voice_agent, group, name):
    # color names that need to have 'to the color' added when using va.speak
    weird_names = ['bisque', 'cornsilk', 'deep pink', 'deep sky blue', 'gainsboro', 'honeydew', 'hot pink', 'khaki',
                    'old lace', 'peru', 'plum', 'rosy brown', 'slate blue', 'spring green', 'tan', 'wheat']
    modifiers = ['pale', 'web']
    modifier_found = False
    for modifier in modifiers:
        if modifier in name:
            # print(modifier, 'in', name)
            modifier_found = True
    # print('light' in name)
    if name in weird_names:
        # added_str = 'to the color '
        launch_word = 'set'
        added_str = ''
        emphasis_level = 'strong'
    elif modifier_found:
        # added_str = 'to the color '
        launch_word = 'turn'
        added_str = ''
        emphasis_level = "moderate"
    elif 'light' in name:
        # added_str = 'to the color '
        launch_word = 'turn'
        added_str = 'to '
        emphasis_level = "moderate"
    else:
        launch_word = 'set'
        added_str = ''
        emphasis_level = "moderate"
    success = va.speak(f'{launch_word} the {group} {added_str}<emphasis level="{emphasis_level}"> {name} </emphasis>, <break time="1s"/>')
    # print(success)
    return {'success': success, 'data': None}
    # sleep(15)

def set_cct(group, cct):
    emphasis_level = "moderate"
    success = va.speak(f'set the {group} to <emphasis level="{emphasis_level}"> {cct} </emphasis> degrees Kelvin, <break time="1s"/>')
    # print(success)
    return {'success': success, 'data': None}
    # sleep(15)

def make_warm_cool(group, value):
    emphasis_level = "moderate"
    print(color_name)
    success = va.speak(f'make {group} <emphasis level="{emphasis_level}"> {value} </emphasis>, <break time="1s"/>')
    # print(success)
    return {'success': success, 'data': None}
    # sleep(15)

def median(readings):
    readings.sort()
    # print(readings)
    indexer = int(len(readings)/2)
    median = readings[indexer]
    return median

def get_cct():
    tcs.gain = 4
    # tcs.integration_time = 100
    readings = []
    while len(readings) <= 10:
        readings.append(round(tcs.color_temperature))
        sleep(0.25)
    cct_value = median(readings)
    return cct_value

def get_lux():
    readings = []
    while len(readings) <= 10:
        readings.append(round(tsl.lux))
        sleep(0.25)
    lux_value = median(readings)
    return lux_value

def get_rgb():
    # tcs.gain = 16
    tcs.gain = 60
    # tcs.integration_time = 100
    readings = []
    while len(readings) <= 10:
        readings.append(tcs.color_rgb_bytes)
        sleep(0.25)
    rgb_value = median(readings)
    return rgb_value

def validate_brightness(voice_agent, brightness, color):
    print('Checking brightness...')
    margin = 2000
    median = get_lux()
    print('median =', median)
    (b0, b1, b2) = color.get(voice_agent).get('lux_coeff')
    prediction = round(brightness*brightness*b2 + brightness*b1 + b0)
    print('prediction =', prediction)
    print('difference =', prediction - median)
    diff = prediction - median
    if abs(diff) <= margin:
        print('SUCCESS!!! Coreect brightness detected!')
        return {'success': True, 'data': None}
    else:
        print('Brightness (lux) =', median)
        print('Looking for:', prediction, f'+/- {margin}')
        return {'success': False, 'data': None}

def validate_color(voice_agent, color):
    print('Checking color...')
    margin_pct = 0.2
    margin_min = 3
    margin_max = 25
    (r, g, b) = color.get(voice_agent).get('tcs_color_100')
    r_error = round(margin_pct*r)
    g_error = round(margin_pct*g)
    b_error = round(margin_pct*b)
    r_margin = margin_min if r_error < margin_min else margin_max if r_error > margin_max else r_error
    g_margin = margin_min if g_error < margin_min else margin_max if g_error > margin_max else g_error
    b_margin = margin_min if b_error < margin_min else margin_max if b_error > margin_max else b_error
    median = get_rgb()
    print('median =', median)
    print('Color values should be', (r, g, b))
    r_diff = r - median[0]
    g_diff = g - median[1]
    b_diff = b - median[2]
    print('r difference =', r_diff, '\tr_margin =', r_margin)
    print('g difference =', g_diff, '\tg_margin =', g_margin)
    print('b difference =', b_diff, '\tb_margin =', b_margin)
    if abs(r_diff) <= r_margin and abs(g_diff) <= g_margin and abs(b_diff) <= b_margin:
        print('SUCCESS!!! Correct color detected!')
        return {'success': True, 'data': None}
    else:
        print(f'Looking for difference values less than {margin_pct*100}%!')
        return {'success': False, 'data': median}

def validate_cct(voice_agent, color):
    print('Checking CCT...')
    cct = color.get(voice_agent).get('color_values')
    if cct > 4500:
        margin = 150
    else:
        margin = 75
    calculated_sensor_value = round(0.6091*cct + 986.41)
    print('calculated_sensor_value =', calculated_sensor_value)
    median = get_cct()
    print('median =', median)
    cct_diff = calculated_sensor_value - median
    print('difference =', cct_diff)
    if abs(cct_diff) <= margin:
        print('SUCCESS!!! Coreect CCT detected!')
        return {'success': True, 'data': None}
    else:
        print(f'Looking for a difference less than {margin}!')
        return {'success': False, 'data': None}





#############################################################################################################################
#                                                                                                                           #
#                                                   DAVEY'S PLAYGROUND                                                      #
#                                                                                                                           #
#############################################################################################################################

# data = {
#     'firstname': 'David',
#     'lastname': 'Bauer'
# }

# with open('config.json', 'w') as outfile:
#     json.dump(data, outfile)

# with open('config.json', 'r') as infile:
#     data = json.load(infile)

# print(data)
# print(data['firstname'])

# set_power_BLE(mac, 'on', '', '')
# set_cct_BLE(mac, 50, '', '')
# set_cct_BLE(mac, 14, '', '')  # -cctVal=14 will equal Google's or Alexa's cct for "incandescent"

# for color in va.rgb_color_list:
#     print(color)
#     (r, g, b) = color[voice_agent]['color_values']
#     set_rgb_BLE(mac, r, g, b, '', '')
#     sleep(5)

# print(va.wake_word)
# for color in va.cct_color_list:
#     print(color['name'])

# set_power(group_name, ['off', 'on', 'off', 'on'])

# set_brightness(group_name, ['72%', '0%', '3%', '125%'])

# set_brightness(group_name, ['0%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['9%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['100%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])
# set_brightness(group_name, ['92%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])

# set_brightness(group_name, ['100%'])
# color = va.cct_color_list[random.randint(0, len(va.cct_color_list) - 1)]
# set_color(group_name, [color])


# if voice_agent == 'alexa':
#     set_color(voice_agent, group_name, ['candlelight'])
#     make_warm_cool(group_name, ['cooler', 'cooler', 'cooler', 'cooler', 'cooler', 'cooler'])
    # set_color(voice_agent, group_name, ['cool white'])
    # make_warm_cool(group_name, ['warmer', 'warmer', 'warmer', 'warmer', 'warmer', 'warmer'])


# color_index = next((index for (index, d) in enumerate(va.cct_color_list) if d['name'] == 'antique white'), None)
# # color_list = []
# # for x in range(5):
# #     color_list.append(va.rgb_color_list[random.randint(0, len(va.rgb_color_list) - 1)])
# for color in va.cct_color_list[color_index:]:
#     success = False
#     attempts = 0
#     color_name = color['name']
#     while not success and attempts < 3:
#         print(f'Trying to validate {color_name}... Take {attempts + 1}...')
#         set_color(voice_agent, group_name, color_name)
#         sleep(5)
#         check_color = validate_cct(voice_agent, color)
#         if check_color['success']:
#             success = True
#             # attempts = 0
#         else:
#             attempts += 1
#             sleep(5)
#     if not success:
#         print(f'Unable to validate {color_name}!')
#         with open("color_failures.txt", "a") as out:
#              out.write(color_name)
#             #  out.write(str(check_color['data']) + '\n')
#     print()


# color_index = next((index for (index, d) in enumerate(va.rgb_color_list) if d['name'] == 'moccasin'), None)
# color_list = va.rgb_color_list
# color_list = []
# for x in range(10):
#     color_list.append(va.rgb_color_list[random.randint(0, len(va.rgb_color_list) - 1)])
# set_brightness(group_name, 100)
# sleep(5)
# for color in color_list[color_index:]:
#     success = False
#     attempts = 0
#     color_name = color['name']
#     while not success and attempts < 3:
#         print(f'Trying to validate {color_name}... Take {attempts + 1}...')
#         set_color(voice_agent, group_name, color_name)
#         sleep(5)
#         check_color = validate_color(voice_agent, color)
#         if check_color['success']:
#             success = True
#             # attempts = 0
#         else:
#             attempts += 1
#             sleep(5)
#     if not success:
#         print(f'Unable to validate {color_name}!')
#         with open("color_failures.txt", "a") as out:
#              out.write(color_name + ' ')
#              out.write(str(check_color['data']) + '\n')
#     print()


# color_index = next((index for (index, d) in enumerate(va.rgb_color_list) if d['name'] == 'red'), None)
# print(color_index)
# color = va.rgb_color_list[color_index]
# print(color)
# set_color(voice_agent, group_name, color['name'])
# sleep(5)
# print('tsl_brt_100   =', get_lux())
# print('tcs_color_100 =', get_rgb())
# brightness = 100
# check_success = set_brightness(group_name, f'{brightness}%')
# sleep(5)
# validate_brightness(voice_agent, brightness, color)
# validate_color(voice_agent, color)


# brt_readings = []
# color_readings = []
# for value in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
#     check_success = set_brightness(group_name, f'{value}%')
#     if check_success['success']:
#         sleep(3)
#         median_brt = get_lux()
#         brt_readings.append(round(median_brt))
#         median_color = get_cct()
#         color_readings.append(median_color)
# for item in brt_readings:
#     print(item)
# for item in color_readings:
#     print(item)

# slope = round((median_100 - median_5) / 95, 2)
# print('m             =', slope)
# supported_colors_list[color_index][voice_agent].update({'slope': slope})
# offset = round(median_75 - (slope * 75), 2)
# supported_colors_list[color_index][voice_agent].update({'offset': offset})
# print('b             =', offset)


# for color in va.rgb_color_list:
#     set_color(voice_agent, group_name, color['name'])
#     sleep(5)
#     success = validate_color(voice_agent, color)
#     if success['success']:
#         x_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#         # x_values = [80, 90, 100]
#         y_values = []
#         # x = np.array(values).reshape((-1, 1))
#         for value in x_values:
#             set_brightness(group_name, [f'{value}%'])
#             sleep(5)
#             new_y_value = get_lux()
#             y_values.append(new_y_value)
#         # y = np.array(y_values)
#         with open("brightness_config.txt", "a") as out:
#             out.write(color['name'] + '\n')
#             for value in y_values:
#                 out.write(str(value) + '\n')
#         # x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
#         # model = LinearRegression().fit(x_, y)
#         # print('coefficients:', model.coef_)


# # sensor_values = {}
# for color in va.cct_color_list:
#     success = set_color(voice_agent, group_name, color['name'])
#     if success['success']:
#         sleep(5)
#         # color_name = color['name']
#         cct_value = color.get(voice_agent).get('color_values')
#         # cct_value = get_cct()
#         # print(cct_value)
#         # sensor_values[f'{color_name}'] = str(cct_value)
#         validate_cct(voice_agent, cct_value)
#         print()
# # print(sensor_values)


# for cct in [2000, 2800, 3100]:
#     set_cct(group_name, cct)
#     sleep(5)
#     validate_cct(voice_agent, cct)
#     print()


# color_index = next((index for (index, d) in enumerate(va.rgb_color_list) if d['name'] == 'yellow green'), None)
# for color in va.rgb_color_list[color_index:]:
# for color in va.rgb_color_list:
#     set_color(voice_agent, group_name, color['name'])
#     sleep(5)
#     print(get_lux())
#     print(get_rgb())
#     print()
#     sleep(5)



# color_index = next((index for (index, d) in enumerate(va.cct_color_list) if d['name'] == 'soft white'), None)
# color = va.cct_color_list[color_index]
# color_name = color['name']
# set_color(voice_agent, group_name, color_name)
# sleep(5)
# set_brightness(group_name, 100)
# sleep(5)
# success = validate_cct(voice_agent, color)
# if success['success']:
#     x_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     # x_values = [80, 90, 100]
#     y_values = []
#     # x = np.array(values).reshape((-1, 1))
#     for value in x_values:
#         set_brightness(group_name, [f'{value}'])
#         sleep(5)
#         new_y_value = get_lux()
#         y_values.append(new_y_value)
#     # y = np.array(y_values)
#     with open("brightness_config.txt", "a") as out:
#         out.write(color['name'] + '\n')
#         for value in y_values:
#             out.write(str(value) + '\n')
    # x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
    # model = LinearRegression().fit(x_, y)
    # print('coefficients:', model.coef_)


# color_index = next((index for (index, d) in enumerate(va.cct_color_list) if d['name'] == 'soft white'), None)
# color = va.cct_color_list[color_index]
# color_name = color['name']
# set_color(voice_agent, group_name, color_name)
# sleep(5)
# for brightness in [12, 20, 24, 50, 6, 33, 100, 5]:
#     success = False
#     attempts = 0
#     while not success and attempts < 3:
#         print(f'Trying to validate brightness for {color_name} at {brightness}%... Take {attempts + 1}...')
#         set_brightness(group_name, brightness)
#         sleep(5)
#         check_brightness = validate_brightness(voice_agent, brightness, color)
#         if check_brightness['success']:
#             success = True
#             # attempts = 0
#         else:
#             attempts += 1
#             sleep(5)
#     if not success:
#         print(f'Unable to validate brightness for {color_name} at {brightness}%!')
#         with open("brightness_failures.txt", "a") as out:
#              out.write(color_name)
#             #  out.write(str(check_color['data']) + '\n')
#     print()

# while True:
#     print('cct =', get_cct())
#     print('lux =', get_lux())
#     print('rgb', get_rgb())


#  DONE: need to redo tcs_color with tcs.gain at 60