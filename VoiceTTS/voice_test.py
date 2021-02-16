from Voice_agent import Voice_agent
from supported_colors import supported_colors_list
import random
import board
import busio
import adafruit_tsl2591
import adafruit_tcs34725
import adafruit_tca9548a
from time import sleep

# Alexa Voice Service protocol (what I think the C by GE Skill maps to, at least)
#
#                                                         | slot |
#     Alexa,     set     <device_name>/<group_name>    to   red.
# | wake word | launch |      invocation name       | utterance (the intent of the command)

def set_power(group, value):
    emphasis_level = 'moderate'
    success = va.speak(f'turn <emphasis level="{emphasis_level}"> {value} </emphasis> the {group}, <break time="1s"/>')
    print(success)
    return success
    # sleep(15)

def set_brightness(group, value):
    if value == 'dim' or value == 'brighten':
        added_str = ''
        launch_word = value
        emphasis_level = 'moderate'
    else:
        added_str = f'to {value}'
        launch_word = 'set'
        emphasis_level = 'none'
    success = va.speak(f'<emphasis level="{emphasis_level}"> {launch_word} </emphasis> the {group} {added_str}, <break time="1s"/>')
    print(success)
    return success
    # sleep(15)

def set_color(group, name):
    emphasis_level = "moderate"
    # print('light' in name)
    if 'light' in name or 'tan' in name or 'gainsboro' in name:
        added_str = 'to the color '
    else:
        added_str = ''
    success = va.speak(f'turn the {group} {added_str}<emphasis level="{emphasis_level}"> {name} </emphasis>, <break time="1s"/>')
    print(success)
    return success
    # sleep(15)

def make_warm_cool(group, value):
    emphasis_level = "moderate"
    print(color_name)
    success = va.speak(f'make {group} <emphasis level="{emphasis_level}"> {value} </emphasis>, <break time="1s"/>')
    print(success)
    return success
    # sleep(15)

def median(readings):
    readings.sort()
    indexer = int(len(readings)/2)
    median = readings[indexer]
    return median

def get_cct():
    tcs.gain = 16
    # tcs.integration_time = 100
    readings = []
    while len(readings) <= 10:
        readings.append(round(tcs.color_temperature))
        sleep(0.25)
    readings.sort()
    print(readings)
    cct_value = median(readings)
    return cct_value

def get_lux():
    readings = []
    while len(readings) <= 10:
        readings.append(round(tsl.lux))
        sleep(0.25)
    readings.sort()
    print(readings)
    lux_value = median(readings)
    return lux_value

def get_rgb():
    tcs.gain = 60
    # tcs.integration_time = 100
    readings = []
    while len(readings) <= 10:
        readings.append(tcs.color_rgb_bytes)
        sleep(0.25)
    readings.sort()
    print(readings)
    rgb_value = median(readings)
    return rgb_value

def validate_brightness(voice_agent, brightness, color):
    median = get_lux()
    print('median =', median)
    b2 = color.get(voice_agent).get('b2')
    b1 = color.get(voice_agent).get('b1')
    b = color.get(voice_agent).get('b')
    prediction = round(brightness*brightness*b2 + brightness*b1 + b)
    print('prediction =', prediction)
    print('residual =', prediction - median)
    if prediction-500 < median < prediction+500:
        print('SUCCESS!!!')
    else:
        print('Brightness =', median)
        print('Looking for:', prediction)

def validate_color(voice_agent, color):
    median = get_rgb()
    print('median =', median)
    color_values = color.get(voice_agent).get('tcs_color_100')
    print('tcs_color_100 =', color_values)
    r_diff = color_values[0] - median[0]
    g_diff = color_values[1] - median[1]
    b_diff = color_values[2] - median[2]
    print('r difference =', r_diff)
    print('g difference =', g_diff)
    print('b difference =', b_diff)
    if abs(r_diff) < 3 and abs(g_diff) < 3 and abs(b_diff < 3):
        print('SUCCESS!!!')
    else:
        print('Looking for differnece values less than 3!')

voice_agent = 'google'  # 'alexa' or 'google'
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

# print(va.wake_word)
# for color in va.cct_color_list:
#     print(color['name'])

group_name = 'color bulb'  # 'color bulb' or 'office lights'

# set_power(group_name, ['off', 'on', 'off', 'on'])

# set_brightness(group_name, ['72%', '0%', '3%', '125%', ])

# set_brightness(group_name, ['0%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['9%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['100%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])
# set_brightness(group_name, ['92%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])

# set_brightness(group_name, ['100%'])
# color = va.cct_color_list[random.randint(0, len(va.cct_color_list) - 1)]
# set_color(group_name, [color])


# if voice_agent == 'alexa':
#     set_color(group_name, ['candlelight'])
#     make_warm_cool(group_name, ['cooler', 'cooler', 'cooler', 'cooler', 'cooler', 'cooler'])
    # set_color(group_name, ['cool white'])
    # make_warm_cool(group_name, ['warmer', 'warmer', 'warmer', 'warmer', 'warmer', 'warmer'])

# color_list = []
# color_names = []
# for x in range(5):
#     color_list.append(va.rgb_color_list[random.randint(0, len(va.rgb_color_list) - 1)])
# for color in color_list:
#     color_names.append(color['name'])
# set_color(group_name, color_names)

color_index = next((index for (index, d) in enumerate(va.rgb_color_list) if d['name'] == 'silver'), None)
print(color_index)
color = va.rgb_color_list[color_index]
print(color)
set_color(group_name, color['name'])
sleep(5)
print('tsl_brt_100   =', get_lux())
print('tcs_color_100 =', get_rgb())
# brightness = 100
# check_success = set_brightness(group_name, f'{brightness}%')
# sleep(5)
# validate_brightness(voice_agent, brightness, color)
# validate_color(voice_agent, color)


# brt_readings = []
# color_readings = []
# for value in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100:
#     check_success = set_brightness(group_name, f'{value}%')
#     if check_success['success']:
#         sleep(3)
#         median_brt = get_lux()
#         brt_readings.append(round(median_brt))
#         median_color = get_rgb()
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

#  TODO: need to redo tcs_color with tcs.gain at 60