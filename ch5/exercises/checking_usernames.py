current_users = ["Admin", "Logan", "Bob", "Sue", "John", "Billy"]

new_users = ["Sam", "LOGAN", "billy", "Sarah", "Joe", "James"]

current_user_case_check = []

for user in current_users:
    current_user_case_check.append(user.lower())    

for user in new_users:
    if user.lower() in current_user_case_check:
        print("This username is unavailable. Please choose another name.\n")
    else: print("The chosen username is available.\n")