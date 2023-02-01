#8. *Bombs
#You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. 
#On the last line of input, you will receive indexes - coordinates of several cells separated by a single space, in the following format: 
#"{row1},{column1} {row2},{column2} … {row3},{column3}".
#On those cells, there are bombs. You must detonate every bomb in the order they were given. 
#When a bomb explodes, it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals). 
#One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
#You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).

n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in x.split(",")) for x in input().split())

directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, 1),    # right
    (0, -1),   # left
    (-1, 1),   # top-right
    (-1, -1),  # top-left
    (1, -1),   # bottom-left
    (1, 1),    # bottom-right
    (0, 0),    # current (this should be last)
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*[matrix[r][c]for c in range(n)], sep=" ") for r in range(n)]
