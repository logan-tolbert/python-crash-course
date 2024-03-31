guest_list = ["Stevie Ray Vaughn", "Dimebag Darrell", "Anthony Bourdain", "Ola Englund"]

print(f"{guest_list[0]} will not be able to make it for dinner.")
print()
guest_list[0] = "Spencer"

print(f"Greetings, {guest_list[0]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[1]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[2]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[3]}. You are invited for dinner.") 
print()
print("Greetings, I have purchased a new dinner table and will be inviting a few more guests.")
print()
guest_list.insert(0, "Sarah")
guest_list.insert(3, "Chris")
guest_list.append("Tyler")

print(f"Greetings, {guest_list[0]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[1]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[2]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[3]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[4]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[5]}. You are invited for dinner.") 
print(f"Greetings, {guest_list[6]}. You are invited for dinner.") 

print()

print("""Greetings, I regret to inform you that my dinner tables delivery
will be delayed. I am only going to be able to have two people ofver for dinner.""")

guest = guest_list.pop()
print(f"Greetings {guest}, I am very sorry about not being abel to have you over for dinner.\n")
guest = guest_list.pop()
print(f"Greetings {guest}, I am very sorry about not being abel to have you over for dinner.\n")
guest = guest_list.pop()
print(f"Greetings {guest}, I am very sorry about not being abel to have you over for dinner.\n")
guest = guest_list.pop()
print(f"Greetings {guest}, I am very sorry about not being abel to have you over for dinner.\n")
guest = guest_list.pop()
print(f"Greetings {guest}, I am very sorry about not being abel to have you over for dinner.\n")

print(f"Greetings, {guest_list[0]}. You are invited for dinner.\n") 
print(f"Greetings, {guest_list[1]}. You are invited for dinner.\n") 

del guest_list[:]


print("Guest list:", guest_list)