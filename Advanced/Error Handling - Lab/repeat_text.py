#1. So Many Exceptions

#You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.
#It is given a sequence of numbers, separated by a ", ". 
#Iterate through each number by its index, and if the number is smaller or equal to 5, make a multiplication. 
#If the number is larger than 5 and smaller or equal to 10, divide the result by the number. In the end, print the final result.

from io import StringIO
import sys
test_input = '''Hello
2
'''

sys.stdin = StringIO(test_input)


def repeat_text(text, number):
    return text * number


try:
    text = input()
    number = int(input())
    print(repeat_text(text, number))

except ValueError:
    print("Variable times must be an integer")
