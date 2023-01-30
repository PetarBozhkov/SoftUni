#4. Sum Matrix Columns

#Write a program that reads a matrix from the console and prints the sum for each column on separate lines.

#On the first line, you will get matrix sizes in format "{rows}, {columns}". 
#On the next rows, you will get elements for each column separated with a single space.

def read_matrix_func():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    current_matrix = []
    for row in range(number_of_rows):
        row_data = list(map(int, input().split(' ')))
        current_matrix.append(row_data)
    return current_matrix


def get_sum_of_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    cols = len(matrix[0])
    sum_of_columns = []
    for i in range(cols):
        col_sum = 0
        for j in range(rows):
            col_sum += matrix[j][i]
        sum_of_columns.append(col_sum)
    return sum_of_columns


data = get_sum_of_columns()

for num in data:
    print(num)
