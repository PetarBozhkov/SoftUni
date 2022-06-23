def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second_integers, third)
    return result


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))
