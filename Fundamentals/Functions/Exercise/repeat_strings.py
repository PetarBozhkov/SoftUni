#4. Repeat String

#Write a function that receives a string and a counter n. 
#The function should return a new string – the result of repeating the old string n times. 
#Print the result of the function. Try using lambda.

# result = lambda a, b: a * b

def repeat_string(a, b):
    return a * b


string = input()
number = int(input())
print(repeat_string(string, number))

# my solution
# text = input()
# counter = int(input())
# result = text * counter
# print(f"{result}")
