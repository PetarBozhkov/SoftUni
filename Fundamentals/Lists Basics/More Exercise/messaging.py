#2. Messaging
#On the first line, you will receive a sequence of numbers separated by a single space. 
#On the second line, you will receive a string.
#Your task is to write a program that sends a message only using chars from the given string. 
#Each char the program adds to the message should be found by its index. 
#The index you are looking for is the sum of a number's digits from the sequence. 
#If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). 
#When you find a char, you should add it to the message and remove it from the string. 
#It means that for the following index, the text will be with one character less.
#Print the final message.

the_numbers = input().split(' ')
the_string = list(tuple(input()))
result = []

for i in range(len(the_numbers)):
    the_number = 0
    for i2 in range(len(the_numbers[i])):
        the_number += int(the_numbers[i][i2])
    result.append(the_number)
for i in range(len(result)):
    if result[i] > len(the_string):
        result[i] -= len(the_string)
        print(the_string.pop(result[i]), end='')
    else:
        print(the_string.pop(result[i]), end='')
