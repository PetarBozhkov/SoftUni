#1. Capture the Numbers

#Write a program that receives strings on different lines and extracts only the numbers. 
#Print all extracted numbers on a single line, separated by a single space.

import re

expression = r"\d+"
numbs = list()
while True:
    text = input()
    if not text:
        break

    numbs.extend(re.findall(expression, text))
print(" ".join(numbs))
