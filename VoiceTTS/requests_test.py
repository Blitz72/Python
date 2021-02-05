import requests
import json

req = requests.get('https://texttospeech.googleapis.com/v1/voices')
print(req.status_code)
print(req.headers)
print(req.text[0:1000])