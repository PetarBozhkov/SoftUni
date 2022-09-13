#3. Decrypting Messages

#On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines, which will follow. 
#On the next n lines – you will receive a lower and an uppercase letter per line.
#You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.

key_value = int(input())
circle_value = int(input())
the_letter = []
string_value = ''
for v in range(circle_value):
    letter = input()
    the_letter.append(chr(ord(letter)+key_value))
print(f'{string_value.join(the_letter)}')
