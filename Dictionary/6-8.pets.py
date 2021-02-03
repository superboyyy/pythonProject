pet1 = {
    'type': 'dog',
    'name': 'david',
}

pet2 = {
    'type': 'cat',
    'name': 'peter',
}

pet3 = {
    'type': 'parrot',
    'name': 'google',
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['type'].title()}.")