from bs4 import BeautifulSoup
import requests


url = "https://www.profesores.frc.utn.edu.ar/electronica/informaticaii/?pIs=3407"
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')

nombres = soup.find('div',{'class':'txtCmn'}).find_all("a")
lista = []

for link in nombres:
    if '.pdf' in link['href']:
        lista.append(link['href'])

for i in lista:
    print(i)