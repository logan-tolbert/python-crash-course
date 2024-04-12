sandwich_orders = ["ham", "turkey", "roast beef", "tuna", "peanut butter", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"Your {sandwich} sandwich is being made.")

print("\nHere is your order:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()} sandwich")


