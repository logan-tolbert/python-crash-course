my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("canoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)

#  this will not work 
friend_foods = my_foods
# this ties my_foods to friend_foods anything done to friend_foods will affect my_foods and vice versa


