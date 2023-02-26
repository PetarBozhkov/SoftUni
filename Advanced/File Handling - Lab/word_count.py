5. Word Count

Write a program that reads a list of words from the file words.txt and finds how many times each of the words is contained in another file text.txt. Matching should be case-insensitive.

The results should be written to other text files. Sort the words by frequency in descending order.

import os
import re

input_file_path = './input.txt'
words_file_path = './words.txt'
words_dict = {}
words = open(words_file_path, 'r').read().split()
for word in words:
    words_dict[word] = 0


regex = r'[\w\']+'
with open(input_file_path, 'r') as file:
    for line in file:
        matches = re.finditer(regex, line)
        for match in matches:
            name = match.group()
            if name.lower() in words_dict:
                words_dict[name.lower()] += 1

output_file_path = './output.txt'
with open(output_file_path, 'w') as file:
    for word, count in sorted(words_dict.items(), key=lambda x: -x[1]):
        file.write(f'{word} - {count}\n')
