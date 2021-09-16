"""Draft of find duplicate assignment"""

word: str = str(input("Enter a word: "))
i: int = 0
duplicate: bool = False

while i < len(word):
    character = word[i]
    cycle_through: int = i + 1
    while cycle_through < len(word):
        if character == word[cycle_through]:
            duplicate = True
        cycle_through = cycle_through + 1
    i = i + 1

print("Found Duplicate: " + str(duplicate))