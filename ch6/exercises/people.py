
person_1 = {
        "first_name": "Logan",
        "last_name": "Tolbert",
        "age": 35,
        "city": "Dora"
     }

person_2 = {
        "first_name": "Sarah",
        "last_name": "Wyatt",
        "age": 30,
        "city": "Dora"
     }
   
person_3 = {
       "first_name": "Monty",
        "last_name": "Python",
        "age": 60,
        "city": "England"
     }

people = [person_1, person_2, person_3]

for person in people:
    for k, v in person.items():
        print(f"{k.capitalize()}:")
        print(f"{v}\n")

    