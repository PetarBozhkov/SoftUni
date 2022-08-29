#8. *Letters Change Numbers

#John invented a game with numbers and letters from the English alphabet. The game was simple.

#You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:

#· First, if the letter in front of the number is:

#o Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
#o Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
#· Next, if the letter after the number is:
#o Uppercase: subtract its position from the resulting number (starting from 1)
#o Lowercase: add its position to the resulting number (starting from 1)

#The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
#He kindly asks you to write a program that performs the operations described above and sums the final results of each string.

from string import ascii_lowercase

words = input().split()
total_sum = 0
for word in words:
    string_number = [numb for numb in word if numb.isdigit()]
    current_number = int("".join(string_number))
    sum_total = 0
    for i in range(len(word)):
        if word[i].isalpha():
            letter_number = ascii_lowercase.index(word[i].lower())
            if i == 0:
                if word[i].isupper():
                    sum_total = current_number / (letter_number + 1)
                else:
                    sum_total = current_number * (letter_number + 1)
            else:
                if word[i].isupper():
                    total_sum += sum_total - (letter_number + 1)
                else:
                    total_sum += sum_total + (letter_number + 1)
print(f"{total_sum:.2f}")
