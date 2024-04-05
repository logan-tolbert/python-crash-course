people = ["sarah", "phil", "tyler", "spencer"]


favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}


for person in people: 
    if person in favorite_languages:
        print("Thanks for responding.")
    else: 
        print("Please take our poll on your favoritve programming language.")