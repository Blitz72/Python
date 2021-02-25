# Google Cloud Text-to-speech Standard Voices
# en-US-Standard-B  MALE    Fairly decent performance
# en-US-Standard-C  FEMALE  X
# en-US-Standard-D  MALE    X
# en-US-Standard-E  FEMALE  So far so good
# en-US-Standard-G  FEMALE
# en-US-Standard-H  FEMALE
# en-US-Standard-I  MALE
# en-US-Standard-J  MALE

# Google Cloud Text-to-speech Wavenet Voices
# en-US-Wavenet-A  MALE
# en-US-Wavenet-B  MALE
# en-US-Wavenet-C  FEMALE
# en-US-Wavenet-D  MALE
# en-US-Wavenet-E  FEMALE
# en-US-Wavenet-G  FEMALE
# en-US-Wavenet-H  FEMALE
# en-US-Wavenet-I  MALE
# en-US-Wavenet-J  MALE

from supported_colors import supported_colors_list
import os
import subprocess
import pathlib
import hashlib
import html
from google.cloud import texttospeech
from dotenv import load_dotenv
from time import sleep

class Voice_agent:
    def __init__(self, voice_agent, filepath):
        load_dotenv('.env')
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        self.client = texttospeech.TextToSpeechClient()
        self.voice_agent = voice_agent
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            pathlib.Path(self.filepath).mkdir(parents=1, exist_ok=1)
            print(f'Directory created: {self.filepath}')
        else:
            print(f'{self.filepath} already exists. Directory not created.')
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
        print(f'Attempting to say: {self.wake_word}, {message}')
        if not os.path.exists(self.filepath + f'{_filename}.mp3'):
            ssml_text = f'<speak>{self.wake_word}, <break time="1s"/> {message}</speak>'
            synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name="en-US-Wavenet-C",
                # ssml_gender=texttospeech.SsmlVoiceGender.MALE
                ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            error = None
            _response = None
            attempts = 0
            audio_content = False
            while attempts < 3 and not audio_content:
                print('TTS attempts =', attempts)
                try:
                    _response = self.client.synthesize_speech(
                        input=synthesis_input, voice=voice, audio_config=audio_config
                    )
                except Exception as ex:
                    error = ex
                    attempts += 1
                    sleep(2)
                finally:
                    if error:
                        print('Failed to create audio content!')
                        print('google-cloud-texttospeech exception:', error)
                        audio_content = False
                    elif _response:
                        print('Audio content created!')
                        audio_content = True
            if audio_content:
                with open(f"{self.filepath}{_filename}.mp3", "wb") as out:
                    # Write the response to the output file.
                    out.write(_response.audio_content)
                    print(f'Audio content written to file "{self.filepath}{_filename}.mp3"')
        else:
            print(f'{_filename}.mp3 already exists, file not created.')
        error = None
        process = None
        try:
            process = subprocess.check_output(f'omxplayer -o local {self.filepath}{_filename}.mp3', shell=True).decode('utf-8')
        except Exception as ex:
            error = ex
        finally:
            if error:
                print('Subprocess exception:', error)
            elif process:
                if 'have' in process:
                    print('File finished playing successfully!')
                    success = True
                    return {'success': True}


# path = '/home/pi/Python/VoiceTTS/voice_files/'
# alexa = Voice_agent('alexa', path)

# print(alexa.wake_word)
# for color in alexa.cct_color_list:
#     print(color['name'])
# alexa.speak('Davey smells bad. I mean really, REALLY, bad!')