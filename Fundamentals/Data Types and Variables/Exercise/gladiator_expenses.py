#10. * Gladiator Expenses

#As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet, a sword, a shield, and an armor.

#You will receive Peter's lost fights count.

#Every second lost game, his helmet is broken.

#Every third lost game, his sword is broken.

#When both his sword and helmet are broken in the same lost fight, his shield also breaks.

#Every second time his shield brakes, his armor also needs to be repaired.

#You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.

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
