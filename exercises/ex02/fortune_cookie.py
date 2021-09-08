"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730409403"

from random import randint

Option_1: int = 1
Option_2: int = 2
Option_3: int = 3
Option_4: int = 4
random_integer: int = int(randint(1, 4))

print("Your fortune cookie says...")
if random_integer == Option_1:
    print("You will live a long a prosperous life.")
else: 
    if random_integer == Option_2:
        print("You will meet a new friend in the next week.")
    else:
        if random_integer == Option_3:
            print("You will soon find something you have lost.")
        else:
            if random_integer == Option_4:
                print("A new hobby will bring you joy this month.")
print("Now, go spread positive vibes!")