#2. Prime Number Checker

#Write a program to check if a number is prime. A prime number is a natural number greater than 1, not a product of two smaller natural numbers. 
#For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
#The input comes as an integer number.
#The output should be True if the number is prime and False otherwise.

num = int(input())
if num>1:
    for i in range(2,num//2):
        if(num%i)==0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
