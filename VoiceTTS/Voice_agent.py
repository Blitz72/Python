from supported_colors import supported_colors_list
import os
import subprocess
import hashlib
from google.cloud import texttospeech
from dotenv import load_dotenv

class Voice_agent:
    def __init__(self, voice_agent, filepath):
        load_dotenv('.env')
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        self.client = texttospeech.TextToSpeechClient()
        self.voice_agent = voice_agent
        self.filepath = filepath
        if voice_agent == 'alexa':
            self.wake_word = voice_agent
        else:
            self.wake_word = 'hey google'
        self.rgb_color_list = []
        self.cct_color_list = []
        for color in supported_colors_list:
            if color.get(self.voice_agent):
                if color.get(self.voice_agent).get('is_rgb'):
                    self.rgb_color_list.append(color)
                else:
                    self.cct_color_list.append(color)

    def create_filename(self, text):
        # print(text)
        hash = hashlib.sha256()
        hash.update(text.encode('utf-8'))
        # print(hash.hexdigest())
        return hash.hexdigest()
    
    def speak(self, message):
        _filename = self.create_filename(message)
        # print(_filename)
        if not os.path.exists(self.filepath + f'{_filename}.mp3'):
            synthesis_input = texttospeech.SynthesisInput(text=message)
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name="en-US-Standard-B"
                # ssml_gender=texttospeech.SsmlVoiceGender.MALE
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            _response = self.client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            with open(f"{self.filepath}{_filename}.mp3", "wb") as out:
                # Write the response to the output file.
                out.write(_response.audio_content)
                print(f'Audio content written to file "{self.filepath}{_filename}.mp3"')
        else:
            print(f'{_filename}.mp3 already exists, file not created.')
        try:
            process = subprocess.check_output(f'omxplayer -o local {self.filepath}{_filename}.mp3', shell=True).decode('utf-8')
            if 'have' in process:
                print('File finished playing successfully!')
        except Exception as ex:
            print('Subprocess exception:', ex)


# path = '/home/pi/Python/VoiceTTS/voice_files/'
# alexa = Voice_agent('alexa', path)

# print(alexa.wake_word)
# for color in alexa.cct_color_list:
#     print(color['name'])
# alexa.speak('Davey smells bad. I mean really, REALLY, bad!')