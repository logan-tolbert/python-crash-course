class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type


    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}\nCuisine: {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant("Umami", "Asian Fusion")

restaurant.describe_restaurant()
restaurant.open_restaurant()