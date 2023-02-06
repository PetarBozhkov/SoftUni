#1. Flatten Lists
#Write a program to flatten several lists of numbers received in the following format:
#§ String with numbers or empty strings separated by "|"
#§ Values are separated by spaces (" ", one or several)
#§ Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below

numbers = [string.split() for string in input().split("|")]
print(*[' '.join(string) for string in numbers[::-1] if string])
