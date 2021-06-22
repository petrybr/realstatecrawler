import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/condominio_residencial/?pagina={}'

i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
totalhouses = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.',''))

df = pd.DataFrame(
    columns=[
        'title',
        'address',
        'area',
        'rooms',
        'bathroom',
        'garage',
        'price',
        'condoprice',
        'houselink'
    ]
)
i = 0 

while totalhouses > df.shape[0]:
    i += 1
    print(f'Page: {i} \t - \t Houses crawled: {df.shape[0]}')
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
    for house in houses: 
        try:
            title = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            title = None 
        try:
            address = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            address = None 
        try:
            area = house.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
        except:
            area = None 
        try:
            rooms = house.find('li', {'class': 'js-property-detail-rooms'}).span.text.strip()
        except:
            rooms = None 
        try:
            bathroom = house.find('li', {'class': 'js-property-detail-bathroom'}).span.text.strip()
        except:
            bathroom = None 
        try:
            garage = house.find('li', {'class': 'js-property-detail-garages'}).span.text.strip()
        except:
            garage = None 
        try:
            price = house.find('div', {'class': 'property-card__price'}).p.text.strip()
        except:
            price = None 
        try:
            condoprice = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condoprice = None 
        try:
            houselink = 'https://www.vivareal.com.br' + house['href']
        except:
            houselink = None 
        
        df.loc[df.shape[0]] = [
            title,
            address,
            area,
            rooms,
            bathroom,
            garage,
            price,
            condoprice,
            houselink  
        ]


df.to_csv('houses.csv',sep=';',index=False)
