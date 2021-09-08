"""Repeating a beat in a loop."""

__author__ = "730409403"

Beat: str = input("What beat do you want to repeat? ")
Number: int = int(input("How many times do you want to repeat it? "))
minimum: int = 0

while 0 < Number:
    print((Beat + " ") * Number)
    Number = Number - Number
while Number < 0: 
    print("No beat...")
    Number = Number - Number