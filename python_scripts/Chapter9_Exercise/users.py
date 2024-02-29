"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

class User:
    """A class that stores attributes that are contained in a user profile.
    It has a method that prints a summary of the user’s information
    and another method that prints a personalized greeting to the user."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Prints a summary of the user’s information"""
        print("User Details")
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\n")

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"Hello {self.first_name}, {self.last_name}!\n\n")

if __name__=="__main__":
    user = User("Tunde", "Akingbade")
    user2 = User("Shadiat", "Shoremilekun")
    user3 = User("Damilola", "Owomoyepon")
    
    users = [user,user2,user3]
    for user in users:
        user.describe_user()
        user.greet_user()