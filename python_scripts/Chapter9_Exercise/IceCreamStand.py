from Restaurant import Restaurant, IceCreamStand
"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

# flavors = ["Strawberry", "Vanilla", "Banana", "Berry", "Bubble Gum", "Coffee Ice Cream"]

if __name__=="__main__":
    ice_cream = IceCreamStand(
        "The Place", "Ghanian Jollof-Rice","Strawberry",
        "Vanilla", "Banana", "Berry",
        "Bubble Gum", "Coffee Ice Cream"
    )
    
    ice_cream.list_flavor()