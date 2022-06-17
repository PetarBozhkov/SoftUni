budget = float(input())
season = input()
destination = ""
type_of_hotel = ""

if budget <= 100:
    destination == "Bulgaria"
    if season == "summer":
        budget *= 0.7
        type_of_hotel == "Camp"
print(f"Somewhere in {destination}")
print(f"{type_of_hotel} - {budget:.2f}")

budget *= 0.3
type_of_hotel == "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_hotel} - {budget:.2f}")

if budget <= 1000:
    destination == "Balkans"
    season == "summer"
    budget *= 0.6
    type_of_hotel = "Camp"
    print(f"Somewhere in {destination}")
    print(f"{type_of_hotel} - {budget:.2f} ")

elif season == "winter":
    budget *= 0.2
    type_of_hotel == "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{type_of_hotel} - {budget:.2f}")

if budget > 1000:
    destination == "Europe"
    season == "summer" or "winter"
    budget *= 0.1
    type_of_hotel == "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{type_of_hotel} - {budget:.2f}")




