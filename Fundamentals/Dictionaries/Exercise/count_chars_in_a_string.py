#1. Count Chars in a String

#Write a program that counts all characters in a string except for space (" ").
#Print all the occurrences in the following format:
#"{char} -> {occurrences}"

letters = {}
symbols = ''.join(s for s in input().split())
for letter in symbols:
    if letter not in letters.keys():  # not in letters
        letters[letter] = 0
    letters[letter] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")
