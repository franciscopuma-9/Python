import requests
import json

url = "http://httpbin.org/get"
args = {'nombre':'Francisco','apellido':"Puma",'Edad':23}
response = requests.get(url,params=args)
print(response.url)
if response.status_code == 200:
    # response_json = response.json()
    # origin = response_json['origin']
    # print(origin)

    response_json = json.loads(response.text)
    origin = response_json['origin']
    print(origin)