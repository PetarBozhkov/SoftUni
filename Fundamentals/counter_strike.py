initial_energy = int(input())
won_battle_counter = 0

while True:
    command = input()

    if command == "End of battle":
        print(f'Won battles: {won_battle_counter}. Energy left: {initial_energy}')
        break

    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        won_battle_counter += 1

        if won_battle_counter % 3 == 0:
            initial_energy += won_battle_counter

    else:
        print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {initial_energy} energy")
        break
