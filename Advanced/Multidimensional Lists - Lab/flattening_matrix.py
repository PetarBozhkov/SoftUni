#3. Flattening Matrix
#Write a program that receives a matrix and prints the flattened version of it (a list with all the values). 
#For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
#On the first line, you will receive the number of a matrix's rows. 
#On the next rows, you will get the elements for each column separated with a comma and a space ", ".

matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
result = [num for row in matrix for num in row]
print(result)

# number_of_rows = int(input())
# matrix = []
# for row in range(number_of_rows):
#     row_data = list(map(int, input().split(', ')))
#     matrix.append(row_data)
#
# new_matrix = []
#
# for row in matrix:
#     for num in row:
#         new_matrix.append(num)
#
# print(new_matrix)
