import requests
import json

url = 'http://127.0.0.1:8000/analyze/'
data = {'text': 'Text to be analyzed'}

response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(response.json())