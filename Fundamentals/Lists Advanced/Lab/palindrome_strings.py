#4. Palindrome Strings

#On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. 
#First, you should print a list containing all the found palindromes in the sequence. 
#Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

strings = input().split(' ')
searched_palindromes = input()
palindromes = []

for word in strings:
    if word == ''.join(reversed(word)):
        palindromes.append(word)
print(f'{palindromes}')
print(f'Found palindrome {palindromes.count(searched_palindromes)} times')
