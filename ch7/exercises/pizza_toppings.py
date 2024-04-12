prompt = ("\nWhat toppings would you like on your pizza? ")
prompt += ("\n(Enter 'quit' when finished adding toppings to your pizza) ") 

request = ""

while request != 'quit':
    request = input(prompt)
    print(f"Adding {request} to your pizza.")
    
print("Your pizza will be ready shortly.")