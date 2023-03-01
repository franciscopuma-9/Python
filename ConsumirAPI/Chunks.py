import requests
url = 'https://images.unsplash.com/photo-1595433707802-6b2626ef1c91?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80'

response = requests.get(url,stream=True)#Realiza la peticion sin descargar el contenido
with open('imagen.jpg','wb') as file:
    for chunk in response.iter_content(): #Descarga el contenido poco a poco
        file.write(chunk)

response.close()