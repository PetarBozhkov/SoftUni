def smallest_number(some_numbers):
    return min(some_numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
all_numbers = [first_num, second_num, third_num]
min_number = smallest_number(all_numbers)
print(min_number)

# my solution
# number_one = int(input())
# number_two = int(input())
# number_three = int(input())
#
# all_nums = number_one, number_two, number_three
# print(min(all_nums))
