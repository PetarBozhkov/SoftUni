#6. List Manipulator

#Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers. 
#He is not quite happy about it since he hates manipulating lists. 
#They will pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. 
#On the other hand, you love lists (and money), so you decide to try your luck.

#The list may be manipulated by one of the following commands:

#· "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]

#o If the index is outside the boundaries of the list, print "Invalid index"

#o A negative index is considered invalid

#· "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4

#· "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3

#o If there are two or more equal min/max elements, return the index of the rightmost one

#o If a min/max even/odd element cannot be found, print "No matches"

#· "first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]

#· "last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]

#o If the count is greater than the list length, print "Invalid count"

#o If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"

#· "end" - stop taking input and print the final state of the list

def make_digit(matrix:list):
    for i in range(len(matrix)):
        matrix[i] = int(matrix[i])
    return matrix


def is_exchange(index: int, matrix: list):
    if index >= len(matrix) or index < 0:
        print('Invalid index')
    else:
        matrix.extend(matrix[:index+1])
        del matrix[:index+1]
        return matrix


def is_max(matrix:list, current_command):
    max_index = []
    max_value = []
    if current_command == 'even':
        for i in range(len(matrix)):
            if matrix[i] % 2 == 0:
                max_value.append(matrix[i])
        for i in range(len(matrix)):
            if matrix[i] % 2 == 0 and matrix[i] == max(max_value):
                max_index.append(i)
    elif current_command == 'odd':
        for i in range(len(matrix)):
            if matrix[i] % 2 != 0:
                max_value.append(matrix[i])
        for i in range(len(matrix)):
            if matrix[i] % 2 != 0 and matrix[i] == max(max_value):
                max_index.append(i)
    if not max_index:
        print('No matches')
    else:
        print(max(max_index))


def is_min(matrix:list, current_command):
    min_index = []
    min_value = []
    if current_command == 'even':
        for i in range(len(matrix)):
            if matrix[i] % 2 == 0:
                min_value.append(matrix[i])
        for i in range(len(matrix)):
            if matrix[i] % 2 == 0 and matrix[i] == min(min_value):
                min_index.append(i)
    elif current_command == 'odd':
        for i in range(len(matrix)):
            if matrix[i] % 2 != 0:
                min_value.append(matrix[i])
        for i in range(len(matrix)):
            if matrix[i] % 2 != 0 and matrix[i] == min(min_value):
                min_index.append(i)
    if not min_index:
        print('No matches')
    else:
        print(max(min_index))


def first_count(count:int, current_command:str, matrix:list):
    new_matrix = []
    if count == 0:
        print(new_matrix)
    else:
        if current_command == 'even':
            for i in range(len(matrix)):
                if matrix[i] % 2 == 0:
                    new_matrix.append(matrix[i])
        elif current_command == 'odd':
            for i in range(len(matrix)):
                if matrix[i] % 2 != 0:
                    new_matrix.append(matrix[i])
        if len(new_matrix) > count:
            print(new_matrix[:count])
        else:
            print(new_matrix)


def last_count(count:int, current_command:str, matrix:list):
    new_matrix = []
    if count == 0:
        print(new_matrix)
    else:
        if current_command == 'even':
            for i in range(len(matrix)):
                if matrix[i] % 2 == 0:
                    new_matrix.append(matrix[i])
        elif current_command == 'odd':
            for i in range(len(matrix)):
                if matrix[i] % 2 != 0:
                    new_matrix.append(matrix[i])
        if len(new_matrix) > count:
            print(new_matrix[-count:])
        else:
            print(new_matrix)


matrix = input().split(' ')
make_digit(matrix=matrix)
command = input().split(' ')
while command[0] != 'end':
    if 'exchange' in command[0]:
        index = int(command[1])
        is_exchange(index=index, matrix=matrix)
    elif 'max' in command[0]:
        max_index = []
        current_command = command[1]
        is_max(matrix=matrix, current_command=current_command)
    elif 'min' in command[0]:
        min_index = []
        current_command = command[1]
        is_min(matrix=matrix, current_command=current_command)
    elif 'first' in command[0]:
        count = int(command[1])
        current_command = command[2]
        if count > len(matrix):
            print('Invalid count')
        else:
            first_count(count=count, current_command=current_command, matrix=matrix)
    elif 'last' in command[0]:
        count = int(command[1])
        current_command = command[2]
        if count > len(matrix):
            print('Invalid count')
        else:
            last_count(count=count, matrix=matrix, current_command=current_command)
    command = input().split(' ')
print(matrix)
