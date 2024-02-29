"""
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant:
    """The class Restaurant has two attributes: a restaurant_name and a cuisine_type.
    It has two methods describe_restaurant() that prints these two pieces of
    information, and a method called open_restaurant() that prints a message indicating
    that the restaurant is open."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant("The Place", "Ghanian Jollof-Rice")
print(f"No. of Customers served: {restaurant.number_served}")
restaurant.set_number_served(10)
print(f"No. of Customers served: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"No. of Customers served: {restaurant.number_served}")
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
restaurant.open_restaurant()