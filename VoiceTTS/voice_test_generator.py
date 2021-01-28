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

directory = 'voice_files'
parent_dir = '/home/pi/Python/VoiceTTS/'

device_name = 'full color br30'
device_name2 = 'C sleep'
group_name = 'office lights'
launch_word = 'set'

path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
    os.mkdir(path)
    print(f'Directory created: {path}')
else:
    print(f'{path} already exists. Directory not created.')


def create_filename(text):
    print(text)
    hash = hashlib.sha256()
    hash.update(text.encode('utf-8'))
#     print(hash.hexdigest())
    return hash.hexdigest()
    
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
    if voice_agent == 'alexa':
        wake_word = voice_agent
    else:
        wake_word = 'hey google'
    for x in range(5):
        colors.append(color_list[random.randint(0, len(color_list)) - 1])
#     print(wake_word)
    return colors, wake_word


voice_agent = 'google'
colors, wake_word = make_color_list(voice_agent, is_rgb=True)  # voice_agent is either 'alexa' of 'google'


for color in colors:
    color_name = color['name']
    if voice_agent == 'google' and 'light' in color['name']:
        added_str = 'the color'
    else:
        added_str = ''
#     print(color)
    message = f'{wake_word}, {launch_word} {group_name} to {added_str} {color_name}, please'
#     message = f'{wake_word}, make the {device_name2}, cooler, please'
    filename = create_filename(message)
    attempts = 0
    file_creation = False
    if not os.path.exists(path + f'/{filename}.mp3'):
#     print(filename)
#     print(f'{path}/{filename}.mp3')
        while attempts < 3 and not file_creation:
            print('Attempting to save file: take', attempts + 1)
            file = gTTS(message, slow=False)
            try:
                file.save(f'{path}/{filename}.mp3')
                print(f'Saving file: {filename}.mp3')
                file_creation = True
            except Exception as ex:
                print('File save exception:', ex)
                attempts += 1
                sleep(1)           
    else:
        print(f'{filename}.mp3 already exists, file not created.')
    try:
        process = subprocess.check_output(f'omxplayer -o local {path}/{filename}.mp3', shell=True).decode('utf-8')
        if 'have' in process:
            print('File finished playing successfully!')
    except Exception as ex:
        print('Subprocess exception:', ex)
    
    sleep(15)  # end of - for color in colors:

