def is_redhead(name):
    return family[name] == "red"

def find_the_redheads(x):
    global family
    family = x 
    red = filter(is_redhead, family.keys())
    return list(red)


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

