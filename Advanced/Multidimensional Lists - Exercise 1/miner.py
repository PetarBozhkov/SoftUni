#9. *Miner
#You are going to create a game called "Miner".
#First, you will receive the size of a square field in which the miner should move.
#On the second line, you will receive the commands for the miner's movement, separated by a single space. 
#The possible commands are "left", "right", "up" and "down".
#In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
#· * - a regular position on the field
#· e - the end of the route
#· c - coal
#· s - miner
#The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. 
#If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
#When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. 
#In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
#· If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
#· If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
#· If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".

n = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[row][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
