#4. Text Filter

#Write a program that receives a text and a string of banned words, separated by a comma and space ", ". 
#All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
#The ban list will be entered on the first input line and the text - on the second input line.

banned_words = input().split(", ")
text = input()
for banned_word in banned_words:
    while banned_word in text:
        length = len(banned_word)
        text = text.replace(banned_word, length*"*")
print(text)
