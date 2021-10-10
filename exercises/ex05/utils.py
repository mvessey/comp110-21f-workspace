"""List utility functions part 2."""

__author__ = "730409403"


def only_evens(list_num: list[int]) -> list[int]:
    """Picking out even integers."""
    i: int = 0
    even_num: list[int] = []
    while i < len(list_num):
        if list_num[i] % 2 == 0:
            even_num.append(list_num[i])
        i += 1
    return even_num


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """New list of some integer values from intial."""
    beginning_value: int = a
    ending_value: int = b - 1
    index_list: list[int] = []
    i: int = 0
    while i < len(a_list):
        if i >= beginning_value and i <= ending_value:
            index_list.append(a_list[i])
        i += 1
    return index_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines two lists of integers."""
    list_3: list[int] = []
    i: int = 0
    x: int = 0
    while i < len(list1):
        list_3.append(list1[i])
        i += 1
    while x < len(list2):
        list_3.append(list2[x])
        x += 1
    return list_3