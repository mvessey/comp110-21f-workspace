"""An example of for in syntax."""

names: list[str] = ["Madeline", "Emma", "Nia", "Ahmad"]

# example of iterating through names using a while loop
print("While output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for ... in output")
# the following for ... in loops is the same as the while loop
for name in names:
    print(name)