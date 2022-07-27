#1. Invert Values

#Write a program that receives a single string containing positive and negative numbers separated by a single space. 
#Print a list containing the opposite of each number.

list_of_numbers = input().split()
opposite_numbers = []

for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)
