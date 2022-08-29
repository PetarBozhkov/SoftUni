#6. Replace Repeating Chars

#Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

text = input()
output = ""

for i in range(len(text)):
    if i == len(text)-1:
        if text[i-2] != text[-1]:
            output += text[i]
        else:
            output += text[i]
    else:
        if text[i] != text[i+1]:
            output += text[i]
print(output)
