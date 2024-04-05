usernames = []

if usernames:
    for user in usernames:
        if user == "Admin":
            print("Hello admin. Would you like to see a status report?")
        else:
            print(f"Hello, {user}. Thank you for logging in again.")
else:
    print("We need to find some more users!")


