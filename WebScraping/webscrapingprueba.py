import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

precio = soup.find('table', {'class':'cotizaciones'}).find_all('td',{'class':'colCompraVenta'})

precio_compra = str(precio[0].text)
precio_compra = precio_compra.replace('\r', '')
precio_compra = precio_compra.replace(' ','')
precio_compra = precio_compra.split('\n')[1]
precio_venta = str(precio[1].text)
precio_venta = precio_venta.replace('\r','')
precio_venta = precio_venta.replace(' ', '')
precio_venta = precio_venta.split('\n')[1]


print('Precio compra: ' + precio_compra)
print('Precio venta: ' + precio_venta)
