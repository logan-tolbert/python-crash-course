class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type


    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}\nCuisine: {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant("Yi Cuisine", "Asian")
restaurant2 = Restaurant("Los Reyes", "Mexican")
restaurant3 = Restaurant("Swamp Johns", "Cajun")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()