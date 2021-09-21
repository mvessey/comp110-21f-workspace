"""Finding duplicate letters in a word."""

__author__ = "730409403"

word: str = str(input("Enter a word: "))
i: int = 0
duplicate: bool = False

while i < len(word):
    character = word[i]
    cycle: int = i + 1
    while cycle < len(word):
        if character == word[cycle]:
            duplicate = True
        cycle = cycle + 1
    i = i + 1

print("Found duplicate: " + str(duplicate))