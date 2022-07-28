#7. Rounding

#Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().

print(list(map(lambda x: round(float(x)), input().split(' '))))

# my solution
# numbers = input().split(' ')
# round_numbers = []
#
# for num in numbers:
#     round_numbers.append(round(float(num)))
# print(round_numbers)
