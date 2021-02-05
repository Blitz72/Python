from supported_colors import supported_colors_list
import hashlib
from google.cloud import texttospeech
from dotenv import load_dotenv

class Voice_agent:
    def __init__(self, voice_agent, file_path):
        if voice_agent == 'alexa':
            self.wake_word = voice_agent
        else:
            self.wake_word = 'hey google'
        self.file_path = file_path

    def create_filename(self, text):
        # print(text)
        hash = hashlib.sha256()
        hash.update(text.encode('utf-8'))
        # print(hash.hexdigest())
        return hash.hexdigest()
    
    def speak(self, message):
        filename = self.create_filename(message)
        print(filename)
        # if not os.path.exists(path + f'/{filename}.mp3'):


path = 'home/pi/Python/VoiceTTS/voicefiles/'
alexa = Voice_agent('alexa', path)

print(alexa.wake_word)
alexa.speak('Davey smells bad.')