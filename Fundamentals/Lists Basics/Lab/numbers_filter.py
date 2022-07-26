#5. Numbers Filter

#On the first line, you will receive a single number n. On the following n lines, you will receive integers. 
#After that, you will be given one of the following commands:

#· even

#· odd

#· negative

#· positive
#Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())

command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'

numbers = [int(input()) for _ in range(n)]
filtered_numbers = []
command = input()

for num in numbers:
    filter_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_negative and num >= 0) or
        (command == command_positive and num < 0)
    )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)

