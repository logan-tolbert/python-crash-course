favorite_nums = {
    "sarah": [12, 16],
    "bob": [34, 66],
    "sue": [66, 120],
    "jim": [43, 24],
    "logan": [420, 21]
}

for person, number in favorite_nums.items():
    print(f"{person.title()}'s favorite numbers are {number[0]} and {number[1]}")