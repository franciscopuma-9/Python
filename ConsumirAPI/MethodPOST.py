import json

import requests


url = "http://httpbin.org/post"
payload = {'nombre':'Francisco','apellido':"Puma",'Edad':23}
response = requests.post(url,data= json.dumps(payload))

#json post se encarga de serializarlos (pasarlos a json)
#data entonces nosotros nos encargamos de serializarlos
print(response.url)
if response.status_code == 200:
    print(response.content)