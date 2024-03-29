motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# Modifying a list
motorcycles[0] = "ducati"
print(motorcycles)

# Appending elements to the end of a list
motorcycles.append("ducati")
print(motorcycles)

motorcycles2 = []

motorcycles2.append("honda")
motorcycles2.append("yamaha")
motorcycles2.append("suzuki")

# Inserting elements into a list
motorcycles2.insert(0, "ducati")

# Removing and item using delete
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing and item using .pop()
popped_motorcycles = motorcycles2.pop()
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping items from any position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removiing and item by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



