#10. * Mutate Strings

#You will be given two strings. Transform the first string into the second one, letter by letter, starting from the first one. 
#After each interaction, print the resulting string only if it is unique.

#Note: the strings will have the same length.

first_string = input()
second_string = input()
last_string = first_string

for symbol_index in range(len(second_string)):

    left_part = second_string[:symbol_index + 1]
    right_part = first_string[symbol_index + 1:]
    current_string = left_part + right_part

    if current_string == last_string:
        continue

    print(current_string)
    last_string = current_string
