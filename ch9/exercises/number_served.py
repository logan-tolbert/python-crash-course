class Restaurant:


    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.totalOrdersServed = 0


    def describe_restaurant(self):
        print(f"""
              Restaurant: {self.name}
              Cuisine: {self.cuisine}
              """
              )


    def open_restaurant(self):
        print(f"{self.name} is now open!")


    def number_served(self,):
        total_served = self.totalOrdersServed
        print(f"""
              Orders served: {total_served}
              """
              )
    
    def set_number_served(self, num_of_orders):
        self.totalOrdersServed = num_of_orders


    def increment_number_served(self, num_of_orders):
        self.totalOrdersServed += num_of_orders
       

restaurant = Restaurant("Umami", "Asian Fusion")
restaurant.describe_restaurant()

restaurant.number_served()
restaurant.set_number_served(100)
restaurant.number_served()
restaurant.increment_number_served(50)
restaurant.number_served()
