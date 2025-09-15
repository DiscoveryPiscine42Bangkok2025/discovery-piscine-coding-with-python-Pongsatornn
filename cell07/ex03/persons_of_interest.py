def get_birth(person):
    return person["date_of_birth"]

def famous_births(p):
    sort = sorted(p.values(), key=get_birth)
    for person in sort:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)

