#1. Sum Matrix Elements
#Write a program that reads a matrix from the console and prints:
#· The sum of all numbers in the matrix
#· The matrix itself
#On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
#On the next rows, you will get elements for each column separated by a comma and a space ", ".

def read_matrix_func(test=False):
    if test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0]
        ]
    number_of_rows, number_of_columns = map(int, input().split(', '))
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix

matrix = read_matrix_func(test=False)
matrix_elements_sum = sum([sum(current_el) for current_el in matrix])

# for i in range(len(matrix)):
#     current_row = matrix[i]
#     matrix_elements_sum += sum(current_row)

print(matrix_elements_sum)
print(matrix)
