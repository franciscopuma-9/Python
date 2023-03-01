import json
import requests

url = "http://httpbin.org/post"
payload = {'nombre':'Francisco','apellido':"Puma",'Edad':23}
headers = {'Conten-Type':'application/json','access-token':'12345'}

response = requests.post(url,data= json.dumps(payload),headers=headers)

print(response.url)
if response.status_code == 200:
    headers_response = response.headers
    print(headers_response)
    server = headers_response['Server']
    print(server)