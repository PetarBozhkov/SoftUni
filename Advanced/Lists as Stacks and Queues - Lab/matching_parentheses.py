#2. Matching Parentheses
#You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
#Print the result back on the console.

data = input()
indexes = []

for i in range(len(data)):
    ch = data[i]

    if ch == '(':
        indexes.append(i)
    elif ch == ')':
        l = indexes.pop()
        print(data[l:i + 1])
