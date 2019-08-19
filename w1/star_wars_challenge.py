
import requests

species = requests.get('https://swapi.co/api/species')
species_count = species.json()['count']

planets = requests.get('https://swapi.co/api/planets')
planets_count = planets.json()['count']

vehicles = requests.get('https://swapi.co/api/vehicles')
vehicles_count = vehicles.json()['count']


print(f'planets  : {planets_count}')
print(f'species  : {species_count}')
print(f'vehicles : {vehicles_count}')

