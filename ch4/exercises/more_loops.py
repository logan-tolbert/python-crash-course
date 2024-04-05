my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("canoli")
friend_foods.append("ice cream")

print("I like: ")
for food in my_foods:
   print(food)

print()

print("My friend likes: ")
for food in friend_foods:
   print(food)

