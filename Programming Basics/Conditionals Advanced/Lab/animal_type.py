animal = input()

is_mammal = animal == "dog"
is_reptile = animal == "snake" or animal == "tortoise" or animal == "crocodile"

if is_mammal:
    print("mammal")
elif is_reptile:
    print("reptile")
else:
    print("unknown")