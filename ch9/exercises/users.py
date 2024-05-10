class User:
    
    def __init__(self, first_name, last_name, email_address, age):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email_address
        self.age = age

    def describe_user(self):
        print(f"Name: {self.firstName} {self.lastName}\nAge: {self.age}\nEmail: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello {self.firstName}")

user1 = User("Logan", "Tolbert", 35, "logo88205@gmail.com")
user2 = User("Sarah", "Wyatt", 30, "scat@aol.com")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()