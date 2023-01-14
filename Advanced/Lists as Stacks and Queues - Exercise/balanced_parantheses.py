#6. Balanced Parentheses
#You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. 
#A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. 
#There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
#{[()]} - Parentheses are balanced.
#(){}[] - Parentheses are balanced.
#{[(])} - Parentheses are NOT balanced.

from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    left_parenthesis = parentheses.popleft()

    if left_parenthesis in "{([":
        open_parentheses.append(left_parenthesis)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parenthesis}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")
