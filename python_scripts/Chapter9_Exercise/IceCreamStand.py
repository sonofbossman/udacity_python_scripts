from number_served import Restaurant
"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavor(self):
        print("The following are the various ice cream flavors we have:")
        for flavor in self.flavors:
            print(flavor)
# flavors = ["Strawberry", "Vanilla", "Banana", "Berry", "Bubble Gum", "Coffee Ice Cream"]

if __name__=="__main__":
    ice_cream = IceCreamStand(
        "The Place", "Ghanian Jollof-Rice","Strawberry",
        "Vanilla", "Banana", "Berry",
        "Bubble Gum", "Coffee Ice Cream"
    )
    
    ice_cream.list_flavor()