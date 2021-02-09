import Voice_agent
import random
from time import sleep

# Alexa Voice Service protocol (what I think the C by GE Skill maps to, at least)
#
#                                                         | slot |
#     Alexa,     set     <device_name>/<group_name>    to   red.
# | wake word | launch |      invocation name       | utterance (the intent of the command)

def set_power(group, values):
    for value in values:
        print(va.speak(f'turn {value} the {group}, please'))
        sleep(15)

def set_brightness(group, values):
    for value in values:
        if value == 'dim' or value == 'brighten':
            added_str = ''
            launch_word = value
        else:
            added_str = f'to {value}'
            launch_word = 'set'
        print(va.speak(f'{launch_word} the {group} {added_str}, please'))
        sleep(15)

def set_color(group, values):
    for value in values:
        # print(value)
        # if 'light' or 'tan' in value:
        #     added_str = 'the color '
        # else:
        #     added_str = ''
        print(va.speak(f'turn the {group} to the color <emphasis> {value} </emphasis>, please'))
        sleep(15)

def make_warm_cool(group, values):
    for value in values:
        va.speak(f'make {group} {value}, please')
        sleep(15)

voice_agent = 'alexa'  # 'alexa' or 'google'
dir_name = voice_agent.capitalize()
# print(dir_name)

# path to store generated voice files
path = f'/home/pi/Python/VoiceTTS/{dir_name}/voice_files/'

va = Voice_agent.Voice_agent(voice_agent, path)

# print(va.wake_word)
# for color in va.cct_color_list:
#     print(color['name'])

group_name = 'office lights'

# set_power(group_name, ['off', 'on', 'off', 'on'])

# set_brightness(group_name, ['72%', '0%', '3%', '125%', ])

# set_brightness(group_name, ['0%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['9%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# set_brightness(group_name, ['100%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])
# set_brightness(group_name, ['92%', 'dim', 'dim', 'dim', 'dim', 'dim', 'dim'])

# set_brightness(group_name, ['100%'])

# color = va.cct_color_list[random.randint(0, len(va.cct_color_list) - 1)]
# set_color(group_name, [color['name']])

# set_color(group_name, ['candlelight'])
# make_warm_cool(group_name, ['cooler', 'cooler', 'cooler', 'cooler', 'cooler', 'cooler'])
# set_color(group_name, ['cool white'])
# make_warm_cool(group_name, ['warmer', 'warmer', 'warmer', 'warmer', 'warmer', 'warmer'])

color_list = []
color_names = []
for x in range(5):
    color_list.append(va.rgb_color_list[random.randint(0, len(va.rgb_color_list) - 1)])
for color in color_list:
    color_names.append(color['name'])
set_color(group_name, color_names)
