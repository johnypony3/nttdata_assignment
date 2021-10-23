import requests

url = "http://worldtimeapi.org/api/timezone/Europe/London.txt"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
