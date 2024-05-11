class User:
    

    def __init__(self, first_name, last_name, email_address, age):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email_address
        self.age = age
        self.loginAttempts = 0


    def describe_user(self):
        print(f"Name: {self.firstName} {self.lastName}\nAge: {self.age}\nEmail: {self.email}\n")


    def greet_user(self):
        print(f"Hello {self.firstName}")


    def increment_login_attempts(self):
        self.loginAttempts += 1

    def reset_login_attempts(self):
        self.loginAttempts = 0

    
user1 = User("Logan", "Tolbert", 35, "logo88205@gmail.com")

print(user1.loginAttempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.loginAttempts)
user1.reset_login_attempts()
print(user1.loginAttempts)
