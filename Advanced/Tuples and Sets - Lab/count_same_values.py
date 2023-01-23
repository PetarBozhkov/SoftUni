#1. Count Same Values
#You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
#The number must be formatted to the first decimal point.

values = tuple(map(float, input().split(' ')))
values_counter = {}

for value in values:
    if value not in values_counter:
        values_counter[value] = 0
    values_counter[value] += 1

for k, v in values_counter.items():
    print(f'{k} - {v} times')
