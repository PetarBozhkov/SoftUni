#3. Value Cannot Be Negative

#Create your own exception called ValueCannotBeNegative. 
#Write a program that reads five numbers from the console (on separate lines). If a negative number occurs, raise the exception.

class ValueCannotBeNegative(Exception):
    pass

numbers = [int(input()) for _ in range(5)]
for num in numbers:
    if num < 0:
        raise ValueCannotBeNegative(f'Value cannot be negative number.Convert {num} to {abs(num)}')
