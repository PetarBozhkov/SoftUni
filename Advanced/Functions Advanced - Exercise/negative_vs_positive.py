#1. Negative vs Positive
#You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. 
#Find the total sum of the negatives and positives, and print the following:
#· On the first line, print the sum of the negatives
#· On the second line, print the sum of the positives
#· On the third line:
#o If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
#o If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"
#Note: you will not receive any zeroes in the input.

def print_result(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(n for n in numbers if n > 0)
negative_numbers = sum(n for n in numbers if n < 0)

print_result(positive_numbers, negative_numbers)

# def sum_negative():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num < 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def sum_positive():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num > 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def print_result(positive, negative):
#     print(negative)
#     print(positive)
#
#     if positive > abs(negative):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print(f"The negatives are stronger than the positives")
#
#
# numbers = [int(x) for x in input().split()]
#
# positive_numbers = sum_positive()
# negative_numbers = sum_negative()
#
# print_result(positive_numbers, negative_numbers)
