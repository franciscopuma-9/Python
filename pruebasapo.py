from urllib.request import urlopen
import json

url = "https://random-data-api.com/api/v2/users?size=100"

response = urlopen(url)

data = json.loads(response.read())

for i in data:
    print(i['gender'])

