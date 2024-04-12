ticket_count = int(input("\nEnter the number of tickets: "))
prompt = ("\nPlease enter your age: ")

total = 0

while ticket_count > 0:
    age = int(input(prompt))
    if age > 12:
        price = 15
        print(f"Your ticket price will be: ${price}")
        ticket_count -= 1
        total += price
    if age >= 3 and age <= 12:
        price = 10
        print(f"Your ticket price will be: ${price}")
        ticket_count -= 1
        total += price
    if age < 3:
        price = 0
        print(f"Your ticket price will be: ${price}")
        ticket_count -= 1
        total += price
        
        
print(f"\nYour total is: ${total}")
print("Enjoy the movie!")
