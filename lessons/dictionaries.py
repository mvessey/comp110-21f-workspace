"""Demonstrations of dictionary capabilities."""

# declaring the type of a dictionary
schools: dict[str, int]

# intialize to an empty dictionary
schools = dict()

# set a key-value ppairing in the dictionary
schools["UNC"] = 19400
schools["DUKE"] = 6717
schools["NCSU"] = 26150

# Access a value by its key -- "lookup"
# Note the single quotes around UNC, bc the name"UNC" is in the dictionary you need to use something different
print(f"UNC has {schools['UNC']} students.")

# Removing a key value pair from a dictionary
# by its key
schools.pop("DUKE")

# Test for the existance of a key
is_duke_present: bool = "DUKE" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# print a dictionary literal representation
print(schools)

# Demonstration of dictionary literls
schools = {}   # same as dict()

# alternatively, initalize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
