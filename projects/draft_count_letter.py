letter: str = input("What letter do you want to seach for?: ")
Word: str = input("Enter a word: ")
i: int = 0
letter_count: int = 0

while i < len(Word):
    if Word[i] == letter:
        letter_count = letter_count + 1
    i = i + 1
print(letter_count)


Beat: str = input("What beat do you want to repeat? ")
Number: int = int(input("How many times do you want to repeat it? "))
minimum: int = 0

while Number < minimum:
    print("No beat...")
