"""Counting letters in a string."""

__author__ = "730409403"

letter: str = input("What letter do you want to seach for?: ")
Word: str = input("Enter a word: ")
i: int = 0
letter_count: int = 0

while i < len(Word):
    if Word[i] == letter:
        letter_count = letter_count + 1
    i = i + 1

print("Count: " + str(letter_count))