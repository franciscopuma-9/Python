import requests

url = "http://httpbin.org/get"
args = {'nombre':'Francisco','apellido':"Puma",'Edad':23}
response = requests.get(url,params=args)
print(response.url)
if response.status_code == 200:
    content = response.content
    print(content)