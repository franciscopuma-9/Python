import requests


url = "https://lol.fandom.com/wiki/V5_data:ESPORTSTMNT03_3090237?action=edit"
page = requests.get(url)

print(page.content)
