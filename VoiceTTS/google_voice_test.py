import subprocess
import time
# import os

voice = '-ven+m3'
pitch = '-p65'
speed = '-s135'
amplitude = '-a200'
wake_word = 'Hey Google'


commands = [
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep candle lite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, bloo\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to fifty five percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep, cuhl wite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, red\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to five percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep soft wite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, green\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to one hundred percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn lights in the office to Zero percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word)
]

# for cmd in commands:
#     voice = subprocess.check_output(cmd, shell=True).decode("utf-8")
#     time.sleep(15)

cmd = commands[9]
voice = subprocess.check_output(cmd, shell=True).decode("utf-8")