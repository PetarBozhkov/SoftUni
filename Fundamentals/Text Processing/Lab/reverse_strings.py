#1. Reverse Strings

#You will be given strings on separate lines until you receive an "end" command. 
#Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".

text = input()
while text != 'end':
    reversed_text = text[::-1]
    print(f"{text} = {reversed_text}")

    text = input()
