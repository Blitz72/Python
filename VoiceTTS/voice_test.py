import Voice_agent
import random
from time import sleep

# Alexa Voice Service protocol (what I think the C by GE Skill maps to, at least)
#
#                                                         | slot |
#     Alexa,     set     <device_name>/<group_name>    to   red.
# | wake word | launch |      invocation name       | utterance (the intent of the command)


voice_agent = 'alexa'  # 'alexa' or 'google'
dir_name = voice_agent.capitalize()
# print(dir_name)
path = f'/home/pi/Python/VoiceTTS/{dir_name}/voice_files/'
va = Voice_agent.Voice_agent(voice_agent, path)

# print(va.wake_word)
# for color in va.cct_color_list:
#     print(color['name'])
percentage = random.randint(101, 150)
va.speak(f'turn the color bulb to {percentage}%, please.')