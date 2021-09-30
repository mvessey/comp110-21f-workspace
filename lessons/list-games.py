"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
print(rolls)

# access an individual item
print(rolls[0])
print(rolls[1])

# access length of the list (number of items)
print(len(rolls))

# access the last item of a list
last_index: int = len(rolls) - 1
print(rolls[last_index])
print(rolls[len(rolls) - 1])

