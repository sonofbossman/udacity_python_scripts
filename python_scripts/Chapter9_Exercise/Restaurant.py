"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""

class Restaurant:
    """The class Restaurant has two attributes: a restaurant_name and a cuisine_type.
    It has two methods describe_restaurant() that prints these two pieces of
    information, and a method called open_restaurant() that prints a message indicating
    that the restaurant is open."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavor(self):
        print("The following are the various ice cream flavors we have:")
        for flavor in self.flavors:
            print(flavor)