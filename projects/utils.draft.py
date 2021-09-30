__author__ = "123456789"

from random import randint
i: int = 0
equal: int = 0
all: list[int] = list()
all.append(randint(0, 100))
all.append(randint(0, 100))
all.append(randint(0, 100))


def equal_to(a: int, b: int, c: int) -> bool:
    """Are any values equal to eachother?"""
    all: list[int] = list()
    all.append(randint(0, 100))
    all.append(randint(0, 100))
    all.append(randint(0, 100))
    print(all)
    i: int = 0
    equal: int = 0
    while i < len(all):
        if all[i] == all[0]:
            equal += 1
        if all[i] == all[1] or all[2]:
            equal += 1
        i += 1
    if equal > int(3):
        return True
    else:
        return False


print(equal_to())