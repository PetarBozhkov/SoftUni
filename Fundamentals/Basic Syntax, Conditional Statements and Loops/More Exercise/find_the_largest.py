#1. Find the Largest
#You will be given a number. Print the largest number that can be formed from the digits of the given number.

numbers = list(input())
for number in range(len(numbers)):
    print(max(numbers), end='')
    numbers.remove(max(numbers))
