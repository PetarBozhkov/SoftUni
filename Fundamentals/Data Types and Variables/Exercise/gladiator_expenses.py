number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = number_of_lost_fights // 2
total_swords_broken = number_of_lost_fights // 3
total_shields_broken = number_of_lost_fights // 6
total_armor_broken = total_shields_broken // 2

expenses = total_helmets_broken * helmet_price + \
           total_swords_broken * sword_price + \
           total_armor_broken * armor_price + \
           total_shields_broken * shield_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
