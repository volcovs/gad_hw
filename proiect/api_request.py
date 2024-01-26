import requests
import json

url = "http://127.0.0.1:8000/my_api/api/"

payload = json.dumps({
    "city": "Brasov",
    "country": "Romania"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
