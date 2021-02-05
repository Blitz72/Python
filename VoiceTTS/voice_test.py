import Voice_agent as va


path = '/home/pi/Python/VoiceTTS/voice_files/'
alexa = va.Voice_agent('alexa', path)

# print(alexa.wake_word)
# for color in alexa.cct_color_list:
#     print(color['name'])
alexa.speak(f'{alexa.wake_word}, turn the color bulb to deep pink, please.')