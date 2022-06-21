#numbers = input().split(" ")
#numbers_to_remove = int(input())
#my_list = []

#for i in range(len(my_list)):
   # my_list.append(int(numbers))
   # list.remove(min(my_list))
   # print(my_list)

list_of_numbers = input()
our_list = list_of_numbers.split()
digits_to_remove = int(input())
our_list_int = []
for i in range(len(our_list)):
    our_list_int.append(int(our_list[i]))
for repetitions in range(digits_to_remove):
    our_list_int.remove(min(our_list_int))
result = ", ".join(str(integers) for integers in our_list_int )
print(result)