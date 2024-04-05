rex = {
    "owner": "Sue",
    "name": "Rex",
    "type": "dog",
}

smokey = {
    "owner": "Charlie",
    "name": "Smokey",
    "type": "cat",
}

red = {
    "owner": "Sarah",
    "name": "Red",
    "type": "dog",
}

pets = [rex, smokey, red]

for pet in pets:
    print(f"Pet name: {pet["name"]}")
    print(f"Type: {pet["type"]}")
    print(f"Owner: {pet["owner"]}\n")


