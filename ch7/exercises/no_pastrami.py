sandwich_orders = ["ham", "pastrami", "turkey", "roast beef", "pastrami", "tuna", "peanut butter", "pastrami", "chicken"]
finished_sandwiches = []

print("Order:")
for order in sandwich_orders:
    print(f"{order.capitalize()} sandwich.")

print("\nApologies, but we are out of pastrami today.\n")
while"pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"Your {sandwich} sandwich is being made.")


print("\nHere is your order:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()} sandwich")


