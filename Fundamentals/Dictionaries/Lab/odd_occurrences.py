#6. Odd Occurrences

#Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.

#· Words are given on a single line, space-separated.

#· Print the result elements in lowercase, in their order of appearance

words = input().split(" ")
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
