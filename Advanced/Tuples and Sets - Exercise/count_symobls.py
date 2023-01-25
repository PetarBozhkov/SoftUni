#4. Count Symbols
#Write a program that reads a text from the console and counts the occurrences of each character in it. 
#Print the results in alphabetical (lexicographical) order.

occurrences = {}

for letter in input():
    if letter not in occurrences:
        occurrences[letter] = 0
    occurrences[letter] += 1

for letter, times in sorted(occurrences.items()):
    print(f"{letter}: {times} time/s")
