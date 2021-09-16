"""An exercise in remainders and boolean logic."""

__author__ = "730409403"

variable: int = int(input("Enter an int: "))
divisible_2: float = variable / 2
whole_divisible_2: int = variable // 2
divisible_7: float = variable / 7
whole_divisible_7: int = variable // 7

if float(divisible_2) == float(whole_divisible_2):
    if float(divisible_7) == float(whole_divisible_7):
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if float(divisible_7) == float(whole_divisible_7):
        print("HEELS")
    else:
        print("CAROLINA")