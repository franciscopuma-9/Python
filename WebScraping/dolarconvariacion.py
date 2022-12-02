import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

precio = soup.find('table', {'class':'cotizaciones'}).find_all('td',{'class':'colCompraVenta'})

compra = str(precio[0].text)
compra = compra.replace('\r', '')
compra = compra.replace(' ','')
aux_compra = compra.split('\n')
precio_compra = aux_compra[1]
variacion_compra = aux_compra[2]
venta = str(precio[1].text)
venta = venta.replace('\r','')
venta = venta.replace(' ', '')
aux_venta = venta.split('\n')
precio_venta = aux_venta[1]
variacion_venta = aux_venta[2]

print('Precio compra: ' + precio_compra + ' Variacion: ' + variacion_compra)
print('Precio venta: ' + precio_venta + ' Variacion: ' + variacion_venta)