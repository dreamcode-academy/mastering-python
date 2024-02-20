import requests
import json
'''
response = requests.get('https://example.com', timeout=10)

print(response.status_code)

print(response.headers)

print(response.text)
'''

#HTTP METHODS

#GET

response = requests.get('https://example.com/data', timeout=10)

print(response.json())

#POST

data = {'key': 'value'}

repsonse = requests.post('https://example.com/sumbit', json=data, timeout=10)
print(response.status_code)
