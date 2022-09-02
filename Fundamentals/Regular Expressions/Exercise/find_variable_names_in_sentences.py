#2. Find Variable Names in Sentences

#Write a program that finds all variable names in each string. 
#A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. 
#Extract only their names without the underscore. Try to do this only with regular expressions.
#The output consists of all variable names extracted and printed on a single line, separated by a comma.

import re

text = input()
expression = r"(?<=\s)\_{1}(?P<name>[a-zA-Z0-9]+)\b"
matches = re.finditer(expression, text)
names = list()
for match in matches:
    name = match.group("name")
    names.append(name)
print(",".join(names))
