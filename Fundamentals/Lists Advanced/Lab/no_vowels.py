#1. No Vowels

#Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
#Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

text = input()
no_vowels = ['a', 'o', 'u', 'e', 'i']
result = [character for character in text if character.lower() not in no_vowels]
print(''.join(result))
