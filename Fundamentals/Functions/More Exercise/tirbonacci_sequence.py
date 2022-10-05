#4. Tribonacci Sequence
#In the Tribonacci sequence, every number is formed by the sum of the previous 3.
#Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. 
#You will receive a positive integer number as input.

def tribonacci_sequence(number: int):
    list_of_numbers = [1]
    print(1, end=' ')
    for i in range(number-1):
        sum_of_previous_numbers = sum(list_of_numbers[-3:])
        print(sum_of_previous_numbers, end=' ')
        list_of_numbers.append(sum_of_previous_numbers)



current_number = int(input())
tribonacci_sequence(current_number)
