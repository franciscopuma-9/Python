import requests
import lxml
from bs4 import BeautifulSoup
url = "https://www.leagueoflegends.com/es-mx/champions/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
lista_pj = []
soup = BeautifulSoup(f.content, 'lxml')
pjs = soup.find('section', {"class":"style__Wrapper-sc-13btjky-0 style__ResponsiveWrapper-sc-13btjky-4 fYZbLI hlxshI"}).find_all('a')

for pj in pjs:
  champ = str(pj['href'])
  campeon = champ.replace('-', ' ')
  campeon = campeon.replace('/', '')
  campeon = campeon[14:]
  lista_pj.append(campeon)

with open('Personajes.txt', 'w') as file:
  for x in lista_pj:
    file.write(x+', ')
#
# with open('Champs.tuvieja','w') as tuvieja:
#   for x in lista_pj:
#     tuvieja.write(x+'\n')
