from supported_colors import supported_colors_list
import os
from gtts import gTTS
import random
import subprocess
from time import sleep
import hashlib

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


# def format_filename(filename):
#     formatted_filename = ''
#     name_parts = filename.split(' ')
#     if len(name_parts) <= 1:
#         return filename
#     else:
#         for part in name_parts:
#             formatted_filename += part + '_'
#         return formatted_filename[:-1]

def create_filename(text):
    print(text)
    hash = hashlib.sha256()
    hash.update(text.encode('utf-8'))
#     print(hash.hexdigest())
    return hash.hexdigest()
    

def make_color_list(voice_agent):
    colors = []
    color_list= []
    for color in supported_colors_list:
        if color.get(voice_agent):
            if color.get(voice_agent).get('is_rgb'):
                print(color['name'])
                color_list.append(color)
    if voice_agent == 'alexa':
        wake_word = voice_agent
    else:
        wake_word = 'hey google'
    for x in range(5):
        colors.append(color_list[random.randint(0, len(color_list))]['name'])
#     print(wake_word)
    return colors, wake_word


colors, wake_word = make_color_list('google')  # va_support is either 'Alexa' of 'Google'
print(colors)
print(wake_word)

for color in colors:
    message = f'{wake_word}, turn the lights in the office to {color}, please'
    filename = create_filename(message)
#     print(filename)
#     print(f'{path}/{filename}.mp3')
    attempts = 0
    while attempts < 3:
        try:
            file = gTTS(message)
            if file:
                attempts = 3
            else:
                print('Error creating gTTS file!')
                attempts += 1
        except Exception as ex:
            print(ex)
    if not os.path.exists(path + f'/{filename}.mp3'):
        try:
            file.save(f'{path}/{filename}.mp3')
            print(f'Saving file: {filename}.mp3')
        except Exception as ex:
            print(ex)
    else:
        print('File already exists, file not saved.')
    subprocess.check_output(f'omxplayer -o local {path}/{filename}.mp3', shell=True).decode('utf-8')
    sleep(15)

# files = os.listdir(path)
# for file in files:
# #     print(file)
#     subprocess.check_output(f'omxplayer -o local {path}/{file}', shell=True).decode('utf-8')
#     sleep(15)
#     os.remove(f'{path}/{file}')

    

