# pg.96
# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python"
# }

#  pg.97
# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}.")

# pg.100
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# pg.101
# for name in favorite_languages.keys():
#     print(name.title())

# # produces the same result
# for name in favorite_languages:
#     print(name.title())

# # pg.102
# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")

# if "erin" not in favorite_languages.keys():
#     print("Erin, please take our poll.")

# pg.103
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The following languages have been mentioned.")
# for language in favorite_languages.values():
#     print(language.title())

# pg.104
# print("The following languages have been mentioned.")
# for language in set(favorite_languages.values()):
#     print(language.title())


# pg.109
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"]
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favortie languages are:")
    for language in languages:
        print(f"\t{language.title()}")