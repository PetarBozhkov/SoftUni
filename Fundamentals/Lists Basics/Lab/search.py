#4. Search

#On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. 
#You should add them to a list and print them. 
#After that, you should filter out only the strings that include the given word and print that list too.

number = int(input())
word = input()
list_one = []

for i in range(number):

    current_strings = input()
    list_one.append(current_strings)
print(list_one)

for i in range(len(list_one) -1, -1, -1):
    element = list_one[i]
    if word not in element:
        list_one.remove(element)
print(list_one)

