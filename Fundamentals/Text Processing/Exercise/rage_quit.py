#9. *Rage Quit

#Every gamer knows what rage-quitting means.
#It's when you're just not good enough, and you blame everybody else for losing a game - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.

#Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. 
#He asks for your help.

#He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". 
#You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".

#First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
#Next, print the rage message itself.
#The strings and numbers will not be separated by anything. 
#The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. 
#The input will be given on a single line.

text = input()
output = ""
current_number = "0"
symbols = ""
unique_symbols = set()
for i in range(len(text)):
    if ord(text[i]) in range(58, 127) or ord(text[i]) in range(33, 48):
        unique_symbols.add(text[i].upper())
    if text[i].isdigit():
        current_number += text[i]
    else:
        if int(current_number) > 0:
            output += symbols.upper() * int(current_number)
            current_number = "0"
            symbols = ""
        symbols += text[i]
if int(current_number) > 0:
    output += symbols.upper() * int(current_number)
print(f"Unique symbols used: {len(unique_symbols)}\n{output}")
