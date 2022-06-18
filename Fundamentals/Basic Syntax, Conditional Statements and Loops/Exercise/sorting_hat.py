name = input()

while name != "Welcome!":
    if name == "Voldemort":
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name == str(input())

if name == "Voldemort":
    print("You should not speak of that name!")
else:
    print("Welcome to Hogwarts.")


