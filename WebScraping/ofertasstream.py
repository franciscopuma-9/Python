from bs4 import BeautifulSoup
import requests
import lxml

# url = "https://store.steampowered.com/specials/?l=spanish"
# page = requests.get(url)
# soap = BeautifulSoup(page.content,"lxml")
#
# juegos = soap.find("div", {"class":"partnersaledisplay_SaleSectionTabListContainer_2JpdO SaleSectionTabListContainer"})
#
# print(juegos)

url = "https://www.binance.com/es/trade/BTC_USDT?theme=dark&type=spot"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

price = soup.find('div', {'class':'ShowPrice'})

print(price)