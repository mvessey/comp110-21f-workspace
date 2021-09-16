"""Drawing forests in a loop."""

__author__ = "123456789"

TREE: str = '\U0001F332'
number: int = int(input("Depth: "))
i: int = 1

while i <= number:
    print(TREE * i)
    i = i + 1
