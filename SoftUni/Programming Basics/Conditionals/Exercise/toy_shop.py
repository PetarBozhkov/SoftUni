excursion_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())
num_toys = num_trucks + num_minions + num_puzzles + num_bears + num_dolls + num_puzzles
toys_price = num_trucks * 2 + num_minions * 8.20 + num_bears * 4.10 + num_dolls * 3 + num_puzzles * 2.60
rent = toys_price * 0.10
profit = toys_price - rent
money_left = profit - excursion_price
if num_toys >= 50:
    print(toys_price * 0.25)
if money_left >= excursion_price:
    print(f"Yes! {money_left:.2f} lv left.")
elif money_left <= excursion_price:
    print(f"Not enough money! {money_left:.2f} lv needed.")
