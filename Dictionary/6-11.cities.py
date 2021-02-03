cities = {
    'Suzhou': {
        'Country': 'China',
        'Population': '2000w',
        },

    'New York': {
        'Country': 'America',
        'Population': '500w',
        },
}

for city, information in cities.items():
    print(f"{city}:")

    for info, fact in information.items():
        print(f"\t{info}: {fact}")

for city, information in cities.items():
    country = information['Country']
    population = information['Population']
    print(f"\n{city} is a city in {country} with a population of {population}.")