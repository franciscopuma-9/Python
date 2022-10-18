import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

precio = soup.find('table', {'class':'cotizaciones'}).find_all('td',{'class':'colCompraVenta'})
print(precio)
precio_compra = precio[0].text[34:42]
precio_venta = precio[1].text[34:42]


print('Precio compra: ' + precio_compra)
print('Precio venta: ' + precio_venta)