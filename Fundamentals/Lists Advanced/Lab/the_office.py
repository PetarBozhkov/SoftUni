#7. The Office

#You will receive two lines of input:

#· a list of employees' happiness as a string of numbers separated by a single space

#· a happiness improvement factor (single number).

#Your task is to find out if the employees are generally happy in their office.

#First, multiply each employee's happiness by the factor.

#Then, print one of the following lines:

#· If half or more of the employees have happiness greater than or equal to the average:

#"Score: {happy_count}/{total_count}. Employees are happy!"

#· Otherwise:

#"Score: {happy_count}/{total_count}. Employees are not happy!"

employees = input().split(' ')
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employees))

filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
