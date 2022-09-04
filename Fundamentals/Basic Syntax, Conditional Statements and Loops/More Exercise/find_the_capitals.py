#2. Find the Capitals

#Write a program that takes a single string and prints a list of all the capital letters indices.

letter = input()
all_index = []

for char in range(len(letter)):
    if letter[char].isupper() == True:
        all_index.append(char)
print(all_index)
