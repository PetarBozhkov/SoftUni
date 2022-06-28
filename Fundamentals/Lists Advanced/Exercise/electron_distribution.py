number_of_electrons = int(input())
list_of_filled_shells = []

for current_shell in range(1, number_of_electrons + 1):
    used_electrons = 2 * (current_shell ** 2)
    number_of_electrons -= used_electrons

    if number_of_electrons == 0:
        list_of_filled_shells.append(used_electrons)
        break
    elif number_of_electrons < 0:
        list_of_filled_shells.append(number_of_electrons + used_electrons)
        break
    list_of_filled_shells.append(used_electrons)
print(list_of_filled_shells)