#3. Find Occurrences of Word in Sentence

#Write a program that finds how many times a word is used in a string. 
#The output is a single number indicating the number of times the string contains the word. 
#Note that letter case does not matter – it is case-insensitive.

import re

text = input()
word = input()
matches_word = re.finditer(fr"\b{word}\b", text, re.IGNORECASE)
occurred_words = list()
for match_word in matches_word:
    occurred_words.append(match_word.group())
print(len(occurred_words))
