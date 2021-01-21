import subprocess
import time
# import os

colors = [
    'candlelight', 'cool white', 'warm white', 'daylight', 'incandescent'
]

def format_filename(name):
    formatted_name = ''
    values = name.split(' ')
#     print(values)
    if len(values) < 1:
        formatted_name = values
    else:
        new_name = ''
#         print(len(values))
        for x in range(len(values)):
            new_name += values[x] + '_'
        formatted_name = new_name[:-1]
    return formatted_name


while len(colors) > 0:
    for color in colors:
        filename = format_filename(color)
        try:
            subprocess.check_output("gtts-cli '{}' --output ~/Python/VoiceTTS/Colors/{}.mp3".format(color, filename), shell=True).decode('utf-8')
            colors.remove(color)
            print(colors)
        except Exception as ex:
            print(ex)
#     print(colors)
    #     time.sleep(10)
