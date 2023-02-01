#3. 2x2 Squares in Matrix
#Find the number of all 2x2 squares containing identical chars in a matrix. 
#On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". 
#On the following rows, you will receive characters separated by a single space. 
#Print the number of all square matrices you have found

rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for row in range(int(rows))]

equal_blocks = 0

for row in range(rows-1):
    for i in range(columns - 1):
        symbol = matrix[row][i]

        if matrix[row][i+1] == symbol and matrix[row+1][i] == symbol and matrix[row+1][i+1] == symbol:
            equal_blocks += 1

print(equal_blocks)
