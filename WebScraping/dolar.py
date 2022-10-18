import requests
from bs4 import BeautifulSoup

url = "https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

precio = soup.find('table', {'class':'cotizaciones'}).find_all('td',{'class':'colCompraVenta'})

compra = precio[0].get_text(strip=True, separator=' ')
list_compra = compra.split(' ')
precio_compra = list_compra[0]+list_compra[1]
variacion_compra = list_compra[2]+list_compra[3]

venta = precio[1].get_text(strip=True, separator=' ')
list_venta = venta.split(' ')
precio_venta = list_venta[0]+list_venta[1]
variacion_venta = list_venta[2]+list_venta[3]

print('Precio compra: ' + precio_compra + ' Variacion: ' + variacion_compra)
print('Precio venta: ' + precio_venta + ' Variacion: ' + variacion_venta)