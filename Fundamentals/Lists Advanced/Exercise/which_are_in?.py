list_one = input().split(", ")
list_two = input().split(", ")
substring = []

for first_word in list_one:
    for second_word in list_two:
        if first_word in second_word and not first_word in substring:
            substring.append(first_word)
print(substring)
