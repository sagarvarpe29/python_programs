import requests

url = 'https://api.meteosource.com/currentweather?location=Chicago'
response = requests.get(url)

my_json = response.json()

print(my_json)

