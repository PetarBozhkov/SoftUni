#2. Repeat Strings

#Write a program that reads a sequence of strings, separated by a single space. 
#Each string should be repeated N times, where N is the length of the string. 
#Print the final strings concatenated into one string.

texts = input().split(" ")
output = ""

while texts:
    text = texts.pop(0)
    count = len(text)
    output += count * text
    
print(output)
