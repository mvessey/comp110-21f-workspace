"""Practicing with Numeric Operators, str to int to str!"""

__author__: str = ("730409403")
left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))
_exponential_ = left_hand_side ** right_hand_side
full_division = float(left_hand_side / right_hand_side)
_divison_ = left_hand_side // right_hand_side
division_remainder = left_hand_side % right_hand_side

print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(_exponential_))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(full_division))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(_divison_))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(division_remainder))