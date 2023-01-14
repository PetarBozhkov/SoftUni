#2. Stacked Queries
#You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
#· '1 {number}' – push the number (integer) into the stack
#· '2' – delete the number at the top of the stack
#· '3' – print the maximum number in the stack
#· '4' – print the minimum number in the stack
#It is guaranteed that each query is valid.
#After you go through all the queries, print the stack from top to bottom in the following format:
#"{n}, {n1}, {n2}, ... {nn}"

from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)),
    4: lambda x: print(min(numbers)),

}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)

numbers.reverse()

print(*numbers, sep=", ")
