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

device_name = 'full color br30'
group_name = 'office lights'

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
    color_list = []
    for color in supported_colors_list:
        if color.get(voice_agent):
#             if color.get(voice_agent):  # color.get(voice_agent).get('is_rgb')
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


colors, wake_word = make_color_list('google')  # va_support is either 'Alexa' of 'Google'
print(colors)
# print(wake_word)

for color in colors:
    color_name = color['name']
    message = f'{wake_word}, turn {device_name} to the color {color_name}, please'
    filename = create_filename(message)
    attempts = 0
    file_creation = False
    
    if not os.path.exists(path + f'/{filename}.mp3'):
#     print(filename)
#     print(f'{path}/{filename}.mp3')
        while attempts < 3 and not file_creation:
#             try:
            print('Attempting to save file: take', attempts + 1)
            file = gTTS(message, slow=False)
#             print(dir(file))
#             print(file.get_urls())
    #                 if file:
    #                     attempts = 3
    #                     print(dir(file))
    #                     print('gTTS file created!')
    #                 else:
    #                     print('Error creating gTTS file!')
    #                     attempts += 1
#             except Exception as ex:
#                 attempts += 1
#                 print(f'Trying to create gTTS file again... (take {attempts})')
#                 print('File creation exception:', ex)
            try:
                file.save(f'{path}/{filename}.mp3')
                print(f'Saving file: {filename}.mp3')
                file_creation = True
            except Exception as ex:
                print('File save exception:', ex)
                attempts += 1
                if attempts == 3:
                    file_creation = False
                sleep(1)           
    else:
        print(f'{filename}.mp3 already exists, file not created.')

#     if file_creation:
    try:
        subprocess.check_output(f'omxplayer -o local {path}/{filename}.mp3', shell=True).decode('utf-8')
    except Exception as ex:
        print('Subprocess exception:', ex)
    
    sleep(15)  # end of - for color in colors:

# files = os.listdir(path)
# for file in files:
# #     print(file)
#     subprocess.check_output(f'omxplayer -o local {path}/{file}', shell=True).decode('utf-8')
#     sleep(15)
#     os.remove(f'{path}/{file}')
