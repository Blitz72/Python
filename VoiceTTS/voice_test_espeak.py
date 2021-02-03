from supported_colors import supported_colors_list
import os
from gtts import gTTS
import random
import subprocess
from time import sleep
import hashlib

# Alexa Voice Service protocol (what I think the C by GE Skill maps to, at least)
#
#                                                         | slot |
#     Alexa,     set     <device_name>/<group_name>    to   red.
# | wake word | launch |      invocation name       | utterance (the intent of the command)

# for color in supported_colors_list:
#     print(color)

# directory = 'voice_files'
# parent_dir = '/home/pi/Python/VoiceTTS/'

device_name = 'color bulb'  # color bulb, c sleep, office lights
device_name2 = 'C sleep'
group_name = 'office lights'
launch_word = 'set'

voice = 'en+m1'
amplitude = 250
speed = 155


def get_wake_word(voice_agent):
    if voice_agent == 'alexa':
        wake_word = voice_agent
    else:
        wake_word = 'hey google'
    return wake_word

def initialize(voice_agent):
    power(voice_agent, ['onn'])
    brightness(voice_agent, ['100%'])
    wake_word = get_wake_word(voice_agent)
    message = f'{wake_word} <break time=\'1500ms\'/> set {device_name} to soft white'
    attempts = 0
    print('Attempting to say:', message)
    try:
        process = subprocess.check_output(f'sudo espeak -v{voice} -a{amplitude} -s{speed} -m "{message}"', shell=True).decode('utf-8')
        print(process)
    except Exception as ex:
        print('Subprocess exception:', ex)
    sleep(15)  # end of - brightness()
    
def make_color_list(voice_agent, is_rgb):
#     print(is_rgb)
#     print(voice_agent)
    colors = []
    color_list = []
    for color in supported_colors_list:
        if is_rgb:
            if color.get(voice_agent):
                if color.get(voice_agent).get('is_rgb'):
    #                 print(color['name'])
                    color_list.append(color)
        else:
            if color.get(voice_agent):
                if not color.get(voice_agent).get('is_rgb'):
    #                 print(color['name'])
                    color_list.append(color)
    wake_word = get_wake_word(voice_agent)
    if is_rgb:
        iterations = 5
    else:
        iterations = 1
    for x in range(iterations):
        colors.append(color_list[random.randint(0, len(color_list)) - 1])
#     print(wake_word)
    return colors, wake_word

def power(voice_agent, values):
    wake_word = get_wake_word(voice_agent)
    launch_word = 'turn'
    for value in values:
        message = f'{wake_word} <break time=\'1500ms\'/> {launch_word} {value} {device_name}'
    #     message = f'{wake_word}, make the {device_name2}, cooler'
        attempts = 0
        print('Attempting to say:', message)
        try:
            process = subprocess.check_output(f'sudo espeak -v{voice} -a{amplitude} -s{speed} -m "{message}"', shell=True).decode('utf-8')
#             process = subprocess.check_output("sudo espeak -ven+m7 -ven+m3 -ven+m2 -a300 -s150 -m \"Alexa <break time='1500ms'/> set color bulb to soft white\"", shell=True).decode('utf-8')
            print(process)
#             if 'have' in process:
#                 print('File finished playing successfully!')
        except Exception as ex:
            print('Subprocess exception:', ex)
        sleep(15)  # end of - brightness()

def brightness(voice_agent, values):
    wake_word = get_wake_word(voice_agent)
    for value in values:
        if value == 'dim' or value == 'brighten':
            added_str = ''
            launch_word = value
        else:
            added_str = f'to {value}'
            launch_word = 'set'
        message = f'{wake_word} <break time=\'1500ms\'/> {launch_word} {device_name} {added_str}'
    #     message = f'{wake_word}, make the {device_name2}, cooler'
        attempts = 0
        print('Attempting to say:', message)
        try:
            process = subprocess.check_output(f'sudo espeak -v{voice} -a{amplitude} -s{speed} -m "{message}"', shell=True).decode('utf-8')
            print(process)
        except Exception as ex:
            print('Subprocess exception:', ex)
        sleep(15)  # end of - brightness()

def color_test(voice_agent, is_rgb):
    colors, wake_word = make_color_list(voice_agent, is_rgb)
    for color in colors:
        color_name = color['name']
#         if voice_agent == 'google' and 'light' or 'tan' in color['name']:
#             added_str = 'the color '
#         else:
#             added_str = ''
    #     print(color)
        message = f'{wake_word} <break time=\'1500ms\'/> {launch_word} {device_name} to {color_name}'
    #     message = f'{wake_word}, make the {device_name2}, cooler'
        attempts = 0
        file_creation = False
        file_exists = False
        print('Attempting to say:', message)
        try:
            process = subprocess.check_output(f'sudo espeak -v{voice} -a{amplitude} -s{speed} -m "{message}"', shell=True).decode('utf-8')
            print(process)
        except Exception as ex:
            print('Subprocess exception:', ex)
        sleep(15)  # end of - color_test()



voice_agent = 'alexa'
# initialize(voice_agent)
# power(voice_agent, ['off the', 'on the', 'off the', 'on the'])
# brightness(voice_agent, ['72%', '0%', '3%', '125%'])
# brightness(voice_agent, ['0%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# brightness(voice_agent, ['6%', 'brighten', 'brighten', 'brighten', 'brighten', 'brighten'])
# brightness(voice_agent, ['100%', 'dim', 'dim', 'dim', 'dim', 'dim'])
# brightness(voice_agent, ['88%', 'dim', 'dim', 'dim', 'dim', 'dim', '100%'])
is_rgb = False
color_test(voice_agent, is_rgb)  # voice_agent is either 'alexa' or 'google'
is_rgb = True
color_test(voice_agent, is_rgb)  # voice_agent is either 'alexa' or 'google'


