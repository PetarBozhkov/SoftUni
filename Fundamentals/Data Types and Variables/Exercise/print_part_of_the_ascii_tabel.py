first_char = int(input())
last_char = int(input())
final_char = ''

for characters in range(first_char, last_char + 1):
    final_char += chr(characters) + " "
print(final_char)
