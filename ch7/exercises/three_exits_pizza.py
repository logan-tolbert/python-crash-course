# Conditional
# prompt = ("\nWhat toppings would you like on your pizza? ")
# prompt += ("\n(Enter 'quit' when finished adding toppings to your pizza) ") 

# request = ""

# while request != 'quit':
#     request = input(prompt)

#     if request != 'quit':
#         print(f"Adding {request} to your pizza.")

# print("Your pizza will be ready shortly.")



# Active
# prompt = ("\nWhat toppings would you like on your pizza? ")
# prompt += ("\n(Enter 'quit' when finished adding toppings to your pizza)\n>>> ") 

# request = ""
# active = True
# while active:
#     request = input(prompt)

#     if request != "quit":
#         print(f"Adding {request} to your pizza.")
#     if request == "quit":
#         active = False

# print("Your pizza will be ready shortly.")



# Break
prompt = ("\nWhat toppings would you like on your pizza? ")
prompt += ("\n(Enter 'quit' when finished adding toppings to your pizza)\n>>> ") 

while True:
    request = input(prompt)

    if request == "quit":
        break
    else:
        print(f"Adding {request} to your pizza.")

print("Your pizza will be ready shortly.")