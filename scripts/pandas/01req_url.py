
import requests
url = 'https://tutorials.technology/data/world-population.csv'
response = requests.get(url)

with open('world-population.csv', 'wb') as csv_file:
    csv_file.write(response.content)
