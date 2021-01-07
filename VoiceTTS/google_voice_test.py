from supported_colors import supported_colors_list
import os
from gtts import gTTS
import random
import subprocess
from time import sleep

# for color in supported_colors_list:
#     print(color)

directory = 'voice_files'
parent_dir = '/home/pi/Python/VoiceTTS/'

path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
    os.mkdir(path)
    print(f'Directory created: {path}')
else:
    print(f'{path} already exists. Directory not created.')

colors = []

def format_filename(filename):
    formatted_filename = ''
    name_parts = filename.split(' ')
    if len(name_parts) <= 1:
        return filename
    else:
        for part in name_parts:
            formatted_filename += part + '_'
        return formatted_filename[:-1]


for x in range(5):
    colors.append(supported_colors_list[random.randint(0, len(supported_colors_list))]['name'])

print(colors)

for color in colors:
    filename = format_filename(color)
    print(filename)
    print(f'{path}/google_{filename}.mp3')
    file = gTTS(f'Hey Google, turn the lights in the office {color}')
    file.save(f'{path}/google_{filename}.mp3')

files = os.listdir(path)
for file in files:
    print(file)
    subprocess.check_output(f'omxplayer -o local {path}/{file}', shell=True).decode('utf-8')
    sleep(15)
    os.remove(f'{path}/{file}')

    

