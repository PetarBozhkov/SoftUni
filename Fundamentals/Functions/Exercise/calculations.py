#3. Calculations

#Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
#The input comes as three parameters – an operator as a string and two integer numbers. 
#The operator can be one of the following: "multiply", "divide", "add", "subtract".

def calculation_func(number_a, number_b, operation):
    if operation == 'multiply':
        return number_a * number_b
    elif operation == 'divide':
        return int(number_a / number_b)
    elif operation == 'add':
        return number_a + number_b
    elif operation == 'subtract':
        return number_a - number_b


type_of_operation = input()
first_numbers = int(input())
second_numbers = int(input())
print(calculation_func(first_numbers, second_numbers, type_of_operation))

# my own solution
# my_operator = input()
# number_one = int(input())
# number_two = int(input())
# result = 0
#
# if my_operator == 'multiply':
#    result = number_one * number_two
# elif my_operator == 'divide':
#    result = number_one // number_two
# elif my_operator == 'add':
#     result = number_one + number_two
# elif my_operator == 'subtract':
#     result = number_one - number_two
# print(result)
