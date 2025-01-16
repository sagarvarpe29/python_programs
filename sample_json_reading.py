import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

json = response.json()

print(json)

for mytitle in json:
    if (mytitle['title'] == 'qui est esse'):
        print('Title is : ',mytitle['title'],' ','Body is : ',mytitle['body'])
