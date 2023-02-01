#1. Diagonals
#Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". 
#You should find the matrix's diagonals, prints them and their sum in the format:
#"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
#Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary][::-1])}. Sum: {sum(secondary)}")
