cities = {
    "Birmingham": {
        "state": "Alabama",
        "population": "196,910",
        "fact": "Birmingham is known as the founding city for the recognition of Veterans Day and hosts the nation's oldest and largest Veterans Day celebration."
    },
    "Atlanta": {
        "state": "Georgia",
        "population": "499,127",
        "fact": "Atlanta holds significant historical importance as the birthplace of civil rights leader Dr. Martin Luther King Jr."
    },
    "Miami": {
        "state": "Florida",
        "population": "449,514",
        "fact": "Miami is the only major city to be founded by a woman"
    },
}

for city, info in cities.items():
    print(f"\n{city} Information:\n State: {info["state"]}\n Population: {info["population"]}\n State fact: {info["fact"]}")