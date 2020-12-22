import subprocess
import time
# import os

voice = '-v+m3'
pitch = '-p65'
speed = '-s135'
amplitude = '-a200'
wake_word = 'Alexa'

commands = [
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep candle lite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, bloo\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to 55 percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep, cuhl wite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, red\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to 5 percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn see sleep soft wite\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn office lights, green\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> set lights in the office to 100 percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn lights in the office to Zero percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn lights in the office to 0 percent\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word),
    "espeak {} {} -m {} {} \"{} <break time='1250ms'/> turn off lights in the office\" --stdout | aplay".format(voice, pitch, speed, amplitude, wake_word)
]

# for cmd in commands:
#     voice = subprocess.check_output(cmd, shell=True).decode("utf-8")
#     time.sleep(15)

cmd = commands[10]
voice = subprocess.check_output(cmd, shell=True).decode("utf-8")