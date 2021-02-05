"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

import os
import subprocess
from google.cloud import texttospeech
from dotenv import load_dotenv

path = '/home/pi/Python/GoogleTTSdemo/'

# if not os.path.exists(path):
#     os.mkdir(path)
#     print(f'Directory created: {path}')
# else:
#     print(f'{path} already exists. Directory not created.')

load_dotenv('.env')
os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hey Google, turn the color bulb to red violet!")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("male")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Standard-E"
    # ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output2.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output2.mp3"')

# print(dir(texttospeech.ListVoicesRequest.to_dict()))
# voice_dict = {}
# print(voice.ListVoicesRequest.to_dict())

filename = 'output2.mp3'

try:
    process = subprocess.check_output(f'omxplayer -o local {path}{filename}', shell=True).decode('utf-8')
    if 'have' in process:
        print('File finished playing successfully!')
except Exception as ex:
    print('Subprocess exception:', ex)
