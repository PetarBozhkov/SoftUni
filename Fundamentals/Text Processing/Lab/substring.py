#3. Substring

#On the first line, you will receive a string. On the second line, you will receive a second string. 
#Write a program that removes all the occurrences of the first string in the second until there is no match. At the end, print the remaining string.

removing_word = input()
the_word = input()
while removing_word in the_word:
    the_word = the_word.replace(removing_word, '')
print(the_word)
