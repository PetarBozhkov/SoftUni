#6. Matrix Shuffling
#Write a program that reads a matrix from the console and performs certain operations with its elements. 
#User input is provided similarly to the problems above - first, you read the dimensions and then the data.
#Your program should receive commands in the format: 
#"swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. 
#A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
#· If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly)
#· If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. 
#A negative value makes the coordinates not valid.
#Your program should finish when the command "END" is entered.

def check_valid_index(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols):
        return True

    return False


def swap_command(command, indexes):
    if check_valid_index(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_command(command_type, info)
