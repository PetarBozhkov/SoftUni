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

