rivers = {
    "Nile": "Africa",
    "Amazon": "South America",
    "Yangtze": "China"
}

for river, country in rivers.items():
    print(f"The {river} river is located in the country of {country}.\n") 


for river in rivers.keys():
    print(river)

print()

for country in rivers.values():
    print(country)
