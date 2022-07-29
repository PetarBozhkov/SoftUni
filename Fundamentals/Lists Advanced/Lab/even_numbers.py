#6. Even Numbers

#Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.

number_list = list(map(int, input().split(', ')))

found_indices_or_no = map(
    lambda x: x if number_list[x] % 2 == 0 else 'no',
    range(len(number_list))
)

even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
print(even_indices)
