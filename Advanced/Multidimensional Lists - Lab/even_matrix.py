#2. Even Matrix
#Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested comprehension for that problem.
#On the first line, you will receive the rows of the matrix. 
#On the next rows, you will get elements for each column separated with a comma and a space ", ".

number_of_rows = int(input())
matrix = []

for _ in range(number_of_rows):
    current_row = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
    matrix.append(current_row)

print(matrix)
