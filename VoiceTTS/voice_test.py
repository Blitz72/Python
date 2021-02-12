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
    success = va.speak(f'turn <emphasis level="{emphasis_level}"> {value} </emphasis> the {group}, please')
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
    success = va.speak(f'<emphasis level="{emphasis_level}"> {launch_word} </emphasis> the {group} {added_str}, please')
    print(success)
    return success
    # sleep(15)

def set_color(group, name):
    emphasis_level = "moderate"
    # print('light' in name)
    if 'light' in name or 'tan' in name:
        added_str = 'the color '
    else:
        added_str = ''
    success = va.speak(f'turn the {group} {added_str}<emphasis level="{emphasis_level}"> {name} </emphasis>, please')
    print(success)
    return success
    # sleep(15)

def make_warm_cool(group, value):
    emphasis_level = "moderate"
    print(color_name)
    success = va.speak(f'make {group} <emphasis level="{emphasis_level}"> {value} </emphasis>, please')
    print(success)
    return success
    # sleep(15)

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
is_rgb = True
if is_rgb:
    tcs.gain = 60
else:
    tcs.gain = 16
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

color_index = next((index for (index, d) in enumerate(va.rgb_color_list) if d['name'] == 'blue violet'), None)
print(color_index)
color = va.rgb_color_list[color_index]
print(color)
set_color(group_name, color['name'])
sleep(5)
readings = []
color_readings = []
check_100 = set_brightness(group_name, '100%')
if check_100['success']:
    sleep(2)
    while len(readings) <= 10:
        readings.append(tsl.lux)
        color_readings.append(tcs.color_rgb_bytes)
        sleep(1)
    readings.sort()
    indexer = int(len(readings)/2)
    median_100 = readings[indexer]
    median_color = color_readings[indexer]
    print('100% =', median_100)
readings = []
check_75 = set_brightness(group_name, '75%')
if check_75['success']:
    sleep(2)
    while len(readings) <= 10:
        readings.append(tsl.lux)
        sleep(1)
    readings.sort()
    indexer = int(len(readings)/2)
    median_75 = readings[indexer]
    print('75% =', median_75)
readings = []
check_25 = set_brightness(group_name, '25%')
if check_25['success']:
    sleep(2)
    while len(readings) <= 10:
        readings.append(tsl.lux)
        sleep(1)
    readings.sort()
    indexer = int(len(readings)/2)
    median_25 = readings[indexer]
    print('25% =', median_25)
print('brt_100 =', median_100)
print('tcs_color =', median_color)
slope = round((median_75 - median_25) / 50, 2)
print('m =', slope)
# supported_colors_list[color_index][voice_agent].update({'slope': slope})
offset = round(median_75 - (slope * 75), 2)
# supported_colors_list[color_index][voice_agent].update({'offset': offset})
print('b =', offset)

#  TODO: need to redo tcs_color with tcs.gain at 60