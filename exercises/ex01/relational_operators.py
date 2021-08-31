"""Relational Operators Practice, using boolean!""" 

__author__: str = ("730409403")
left_hand_side: int = int(input("Left hand side: "))
right_hand_side: int = int(input("Right hand side: "))
less_than = bool(left_hand_side < right_hand_side)
greater_than_equal = bool(left_hand_side >= right_hand_side)
_equal_ = bool(left_hand_side == right_hand_side)
not_equal = bool(left_hand_side != right_hand_side)

print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(less_than))
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(greater_than_equal))
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(_equal_))
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(not_equal))