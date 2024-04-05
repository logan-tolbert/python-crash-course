# pg.92

# alien_0 = {"color": "green", "points": 5}

# print(alien_0["color"])
# print(alien_0["points"])

# alien_0 = {"color": "green"}
# print(alien_0["color"])

# alien_0 = {"color": "green", "points": 5}

# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")

# pg.93
# alien_0 = {"color": "green", "points": 5}
# print(alien_0)

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)


# pg.94
# alien_0 = {}

# alien_0["color"] = "green"
# alien_0["points"] = 5

# print(alien_0)

# pg.94-95
# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0["color"]}.")
# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0["color"]}.")

# pg.95
# alien_0 = {"x_postiiton": 0, "y_postition": 25, "speed": "medium"}
# print(f"Original postition: {alien_0['x_postiiton']}")

# # move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "meduim":
#     x_increment = 2
# else:
#     # this must be a fast alien.
#     x_increment = 3

# # The new postition is the old postition plus the increment.
# alien_0["x_postiiton"] = alien_0["x_postiiton"] + x_increment

# print(f"New position: {alien_0["x_postiiton"]}")

# pg.96
alien_0 = {"color": "green", "points": 5}
print(alien_0)
del alien_0["points"]
print(alien_0)