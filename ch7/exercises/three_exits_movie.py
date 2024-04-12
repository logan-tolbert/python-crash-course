#  Conditional
# ticket_count = int(input("\nEnter the number of tickets: "))
# prompt = ("\nWelcome to Python Studios")
# prompt += ("\nPlease enter your age: ")
# total = 0
# 
# while ticket_count > 0:
#     
#     age = int(input(prompt))
#     if age > 12:
#         price = 15
#     if age >= 3 and age <= 12:
#         price = 10
#     if age < 3:
#         price = 05
#     if ticket_count != 0:
#         print(f"Your ticket price will be: ${price}")
#         ticket_count -= 1
#         total += price
        
# print(f"\nYour total is: ${total}")
# print("Enjoy the movie!")



# Active
# ticket_count = int(input("\nEnter the number of tickets: "))
# prompt = ("\nWelcome to Python Studios")
# prompt += ("\nPlease enter your age: ")

# total = 0
# active = True

# while active:
#     age = int(input(prompt))
#     if age > 12:
#         price = 15
#         print(f"Your ticket price will be: ${price}")
#         ticket_count -= 1
#         total += price
#     if age >= 3 and age <= 12:
#         price = 10
#         print(f"Your ticket price will be: ${price}")
#         ticket_count -= 1
#         total += price
#     if age < 3:
#         price = 0
#         print(f"Your ticket price will be: ${price}")
#         ticket_count -= 1
#         total += price
#     if ticket_count == 0:
#         active = False
        
        
# print(f"\nYour total is: ${total}")
# print("Enjoy the movie!")




# Break

prompt = ("Welcome to Python Studios!\nPlease enter your age: ")

total = 0

while True:
    age = input(prompt)
    if str(age) == "quit":
        break
    elif int(age) > 12:
        price = 15
        print(f"Your ticket price will be: ${price}")
        total += price
    elif int(age) >= 3 and int(age) <= 12:
        price = 10
        print(f"Your ticket price will be: ${price}")
        total += price
    elif int(age) < 3:
        price = 0
        print(f"Your ticket price will be: ${price}")
        total += price
           
        
print(f"\nYour total is: ${total}")
print("Enjoy the movie!")