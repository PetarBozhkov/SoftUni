#3. Elevator

#Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons. 
#The input holds two lines: the number of people N and the capacity P of the elevator.

import math
number_of_people = int(input())
capacity = int(input())
courses = math.ceil(number_of_people / capacity)

print(courses)
