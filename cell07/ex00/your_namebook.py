def array_of_names(p):
    name = []
    for first,last in p.items():
        full_name = first.capitalize() + " " + last.capitalize()
        name.append(full_name)
    return name

pdas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "miel",
    "fifi": "brindacier"
}

print(array_of_names(pdas))
