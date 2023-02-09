#6. Operate

#Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). 
#The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below.
#Submit only your function in the Judge system

def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(*args):
        numbs = [x for x in args]
        result = numbs.pop(0)
        for numb in numbs:
            result -= numb
        return result


    def multiplication(*args):
        result = 1
        for numb in args:
            result *= numb
        return result

    def division(*args):
        numbs = [x for x in args]
        result = numbs.pop(0)
        for numb in numbs:
            result /= numb
        return result

    operators = {
        '+': add,
        '-': subtract,
        '*': multiplication,
        '/': division,
    }

    return operators[operator](*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate('/', 10, 2))
print(operate('-', 10, 2))
