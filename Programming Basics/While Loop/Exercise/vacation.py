needed_money_for_excursion = float(input())
current_money = float(input())
spending_counter = 0
total_days = 0
spending_too_many_days = False

while current_money < needed_money_for_excursion:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == "save":
        current_money += current_sum
        spending_counter = 0
    else:
        spending_counter += 1
        if spending_counter == 5:
            spending_too_many_days = True
            break
        current_money -= current_sum
        if current_money < 0:
            current_money = 0

if spending_too_many_days:
    print(f"You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")


