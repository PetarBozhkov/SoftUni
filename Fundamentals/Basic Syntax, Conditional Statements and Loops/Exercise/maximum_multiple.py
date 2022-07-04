# 4. Maximum Multiple

# On the first line, you will be given a positive number, which will serve as a divisor. 
# On the second line, you will receive a positive number that will be the boundary. You should find the largest integer N, that is:

# · divisible by the given divisor

# · less than or equal to the given bound

# · greater than 0

# Note: it is guaranteed that N is found.

divisor = int(input())
boundary = int(input())
max_multiplier = 0

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        max_multiplier = current_number
        break

print(max_multiplier)
