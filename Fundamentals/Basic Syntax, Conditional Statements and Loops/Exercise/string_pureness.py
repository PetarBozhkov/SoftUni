#6. String Pureness

#You will be given number n.
#After that, you'll receive different strings n times. 
#Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":

#· If a string is pure, print "{string} is pure."

#· Otherwise, print "{string} is not pure!"

number_of_strings = int(input())

for string in range(number_of_strings):
    text = input()
    if '.' in text or ',' in text or '_' in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")
