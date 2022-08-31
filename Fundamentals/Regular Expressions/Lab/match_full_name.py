#1. Match Full Name

#Write a program to match full names from a sequence of characters and print them on the console.

import re
phones = input()
expression = r"\+359([ -])2\1\d{3}\1\d{4}\b"
matches = re.finditer(expression, phones)
phone = list()
for match in matches:
    phone.append(match.group())
print(", ".join(phone))
