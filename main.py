#!python3

import requests

r = requests.get('http://tp2.test/tp2/start')

print(r.text)
