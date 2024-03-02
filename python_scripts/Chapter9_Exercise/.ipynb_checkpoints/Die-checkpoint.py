from random import choice

"""
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        output = choice(1, self.sides)
        print(f"Rolling a {self.sides}-sided die...")
        print(f"Output: {output}\n")

play = Die(10)
play_2= Die(20)

#Rolling each die 10 times
for num_time in range(1,11):
    play.roll_die()
    play_2.roll_die()