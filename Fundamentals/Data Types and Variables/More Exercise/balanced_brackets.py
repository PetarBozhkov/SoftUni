#4. Balanced Brackets
#On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
#· Opening bracket – "(",
#· Closing bracket – ")" or
#· Random string
#Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. 
#Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced. 
#You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.

numb = int(input())
last_value = []
for i in range(numb):
    value = input()
    if '(' in value and '(' not in last_value:
        last_value.append('(')
    elif ')' in value and ')' not in last_value:
        last_value.append(')')
    if ')' in last_value and '(' in last_value:
        last_value.clear()
if ')' in last_value and '(' in last_value or bool(last_value) is False:
    print('BALANCED')
else:
    print('UNBALANCED')
