"""List utility functions."""


__author__ = "730409403"


def all(list_numbers: list[int], number: int) -> bool:
    """Return true if number is found in the list of integers, False others."""
    i: int = 0
    while i < len(list_numbers):
        item: int = list_numbers[i]
        if item != number:
            return False
        i += 1
    if 0 == len(list_numbers):
        return False
    return True


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Finding if lists are equal to eachother."""
    if list1 == list2:
        return True
    else:
        return False


def max(list_numbers: list[int]) -> int:
    """Find the maximum of the list."""
    if len(list_numbers) == 0:
        raise ValueError("max() arg is an empty List")
    if list_numbers[0] > list_numbers[1] and list_numbers[0] > list_numbers[2]:
        return list_numbers[0]
    if list_numbers[1] > list_numbers[0] and list_numbers[1] > list_numbers[2]:
        return list_numbers[1]
    if list_numbers[2] > list_numbers[0] and list_numbers[2] > list_numbers[1]:
        return list_numbers[2]