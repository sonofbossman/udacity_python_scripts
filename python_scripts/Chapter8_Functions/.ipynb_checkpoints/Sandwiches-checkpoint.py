# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich(*items):
    print(
        f"Dear Customer,\n\nYou just placed an order of sandwich with the following items:\n"
    )
    for item in items:
        print(item)
    print("\nRegards\n")

make_sandwich("Honey","Meat","Yellow Beans","Plantains")
make_sandwich("Fish","Salad","Fruits")
make_sandwich("Jam","Chicken","Fried Egg")