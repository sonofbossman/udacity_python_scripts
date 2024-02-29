"""
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User:
    """A class that stores attributes that are contained in a user profile.
    It has a method that prints a summary of the user’s information
    and another method that prints a personalized greeting to the user."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user’s information"""
        print("User Details")
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\n")

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"Hello {self.first_name}, {self.last_name}!\n\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Tunde", "Akingbade")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user2 = User("Shadiat", "Shoremilekun")
user3 = User("Damilola", "Owomoyepon")
print("Getting the number of login attempts...")
print(f"Login Attempts: {user.login_attempts}\n")
user.reset_login_attempts()
print("Resetting login attempts...")
print(f"Login Attempts: {user.login_attempts}")
# users = [user,user2,user3]
# for user in users:
#     user.describe_user()
#     user.greet_user()