#10. * Bread Factory

#As a young baker, you are baking the bread out of the bakery.

#You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. 
#Each event is separated with '|' (vertical bar): "event1|event2| … eventN"

#Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")

#· If the event is "rest":

#o You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). 
#Print: "You gained {gained_energy} energy.".

#o After that, print your current energy: "Current energy: {current_energy}.".

#· If the event is "order":

#o You've earned some coins (the number in the second part).

#o Each time you get an order, your energy decreases by 30 points.

#§ If you have the energy to complete the order, print: "You earned {earned} coins.".

#§ Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".

#· In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend.

#o If you have enough money, you should buy the ingredient and print:

#"You bought {ingredient}."

#o Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.

#If you managed to handle all events throughout the day, print on the following 3 lines:

#"Day completed!"

#"Coins: {coins}"

#"Energy: {energy}"

list_of_events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True

for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    number = int(event_info[1])
    if type_of_event == "rest":
        temporary_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            if total_energy > 100:
                total_energy = 100
            print("You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break

# gornoto решение е на Иван Шопов

working_day_events = input().split('|')
initial_energy = 100
initial_coins = 100
is_true = True
for i in working_day_events:
    current_energy = 0
    gained_energy = 0
    info = i.split('-')
    event_or_ingredient = info[0]
    number = int(info[1])
    if event_or_ingredient == 'rest':
        initial_energy += number
        if initial_energy >= 100:
            diff = abs(100 - initial_energy)
            initial_energy -= diff
            current_energy = initial_energy
            gained_energy = number - diff
        else:
            gained_energy = number
            current_energy = initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_or_ingredient == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")
            continue
    else:
        needed_coins = number
        if initial_coins >= needed_coins:
            initial_coins -= needed_coins
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            is_true = False
            break
if is_true:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
