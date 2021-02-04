import requests
import json

req = requests.get('https://adafruit.com')
print(req.status_code)
print(req.headers)
print(req.text[0:1000])