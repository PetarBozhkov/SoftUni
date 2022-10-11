#4. Battle Ships
#You will be given a number n representing the number of rows of the field. 
#On the following n lines, you will receive each field row as a string with numbers separated by a space. 
#Each number greater than zero represents a ship with health equal to the number value.
#After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". 
#Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1. 
#If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.

rows_of_the_field = int(input())
battle_ships = list()

for row in range(rows_of_the_field):
    battle_ships.append(list(map(int, input().split(' '))))
attacks = input().split(' ')
destroyed_ship = 0

for attack in range(len(attacks)):
    attacked_row = int(attacks[attack][0])
    attacked_col = int(attacks[attack][2])
    if battle_ships[attacked_row][attacked_col] > 0:
        battle_ships[attacked_row][attacked_col] -= 1
        if battle_ships[attacked_row][attacked_col] == 0:
            destroyed_ship += 1
print(destroyed_ship)
