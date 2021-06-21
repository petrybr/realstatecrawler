#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/condominio_residencial/?pagina={}'

i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)

# %%
totalhouses = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.',''))
houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})

#%%
house = houses[0]
title = house.find('span', {'class': 'property-card__title'}).text.strip()
address = house.find('span', {'class': 'property-card__address'}).text.strip()
area = house.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
rooms = house.find('li', {'class': 'js-property-detail-rooms'}).span.text.strip()
bathroom = house.find('li', {'class': 'js-property-detail-bathroom'}).span.text.strip()
garage = house.find('li', {'class': 'js-property-detail-garages'}).span.text.strip()
price = house.find('div', {'class': 'property-card__price'}).p.text.strip()
condoprice = house.find('strong', {'class': 'js-condo-price'}).text.strip()
houselink = 'https://www.vivareal.com.br' + house['href']
print(title)
print(address)
print(area)
print(rooms)
print(bathroom)
print(garage)
print(price)
print(condoprice)
print(houselink)