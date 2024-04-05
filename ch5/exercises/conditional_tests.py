print("a" == "a") # True
print("a" == "b") # False
print("a" == "A") # False
print(1 == 1) # True
print(12 == "12") # False

bool_1 = True
bool_2 = True
print(bool_1 == bool_2) # True

cars = ["bmw", "audi", "toyata", "subaru"]

print("subaru" in cars) # True
print("honda" in cars) # False
print("BMW" in cars) # False


print(bool_1 == True and bool_2 == True) # True

print(len("audi") > len("deer")) # Flase
print(len("audi") >= len("deer")) # True

print("a" == "A".lower()) # True
print("audi" not in cars) # False
