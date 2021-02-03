favorite_places = {
    'david': ['suzhou'],
    'peter': ['guangzhou'],
    'judy': ['shanghai', 'beijing'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()}'s favorite places are: ")
    else:
        print(f"{name.title()}'s favorite places is: ")

    for place in places:
        print(f"\t{place.title()}")