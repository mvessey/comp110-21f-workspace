"""Repeating a beat in a loop."""

__author__ = "730409403"

Beat: str = input("What beat do you want to repeat? ")
Number: int = int(input("How many times do you want to repeat it? "))
beats = Beat
i: int = 1

while i < Number:
    beats += " " + Beat
    i = i + 1
if 0 >= Number:
    print("No beat...")
else:
    print(beats)