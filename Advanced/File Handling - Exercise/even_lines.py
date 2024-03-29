#1. Even Lines
#Write a program that reads a text file and prints on the console its even lines. 
#Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

symbols = ["-", ",", ".", "!", "?"]

with open("files/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")
    print(*text[row].split()[::-1], sep=" ")
