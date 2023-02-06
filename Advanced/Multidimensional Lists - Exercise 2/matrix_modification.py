#2. Matrix Modification
#Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. 
#You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
#· "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#· "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
#If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
#When you receive "END", you should print the matrix and stop the program

size = int(input()) 
matrix = [[int(n) for n in input().split()] for _ in range(size)]

command = input().split() 

while command[0] != 'END': 
    type_command, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])
    

    if row < 0 or row >= size or col < 0 or col >= size:  
        print('Invalid coordinates') 
    elif type_command == 'Add':  
        matrix[row][col] += num 
    elif type_command == 'Subtract':  
        matrix[row][col] -= num 

    command = input().split()  

[print(*row) for row in matrix]
