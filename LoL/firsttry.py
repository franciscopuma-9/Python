from bs4 import BeautifulSoup
import requests

url = "https://lol.fandom.com/wiki/V5_data:ESPORTSTMNT03_3090237"
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')

key = soup.find('table',{'class':"mw-json"}).find_all('span')

value = soup.find('table',{'class':"mw-json"}).find_all('td',{'class':"mw-json-value"})

total = [key,value]

print(len(key),len(value))
for i in range(len(value)):
    print(key[i].text + ':' + value[i].text)


