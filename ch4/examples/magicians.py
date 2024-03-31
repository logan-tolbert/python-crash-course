magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

#  will cause error 
#  for magician in magicians:
#  print(magicians)

#  incorrct indentation
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")   

#  Indenting unnecessarily
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")

# forgetting the colon
# for magician in magicians
    # print(magician)
    