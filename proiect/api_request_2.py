import requests

url = "https://v6.exchangerate-api.com/v6/a5ee9b9bb0f8dc73dd2dbdb3/latest/USD"

payload = {}
headers = {
  'Authorization': 'Token a5ee9b9bb0f8dc73dd2dbdb3'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()['conversion_rates']['EUR'])
