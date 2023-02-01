#2. Diagonal Difference
#Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
#On the first line, you will receive an integer N - the size of a square matrix. 
#The following N lines hold the values for each column - N numbers separated by a single space. 
#Print the absolute difference between the primary and the secondary diagonal sums.

num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

primary_sum = 0
secondary_sum = 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[num-i-1][i]

print(abs(primary_sum-secondary_sum))
