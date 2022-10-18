import requests
from bs4 import BeautifulSoup
from get_price import get_price
def main():
    url = "https://www.infodolar.com/cotizacion-dolar-provincia-cordoba.aspx"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    price = soup.find('table', {'class': 'cotizaciones'}).find_all('td', {'class': 'colCompraVenta'})
    delta = soup.find('table', {'class': 'cotizaciones'}).find_all('span', {'class': 'variacionCompraVenta'})
    get_buy = get_price(price,delta, 0)
    get_sell = get_price(price,delta, 1)
    print('Precio compra: ' + get_buy[0] + ' Variacion: ' + get_buy[1])
    print('Precio venta: ' + get_sell[0] + ' Variacion: ' + get_sell[1])

if __name__ == "__main__":
    main()
