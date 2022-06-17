import math

football_fan = input()
first_budget = float(input())
number_beers = int(input())
number_chips = int(input())

beer_price = 1.20
all_beer = number_beers * beer_price
chips_price = all_beer * (45 / 100)
all_chips = math.ceil(chips_price * number_chips)
whole_sum = all_beer + all_chips
difference = abs(first_budget - whole_sum)

if first_budget >= whole_sum:
    print(f"{football_fan} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{football_fan} needs {difference:.2f} more leva!")

