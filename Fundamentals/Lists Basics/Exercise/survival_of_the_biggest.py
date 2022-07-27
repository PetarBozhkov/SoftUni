#6. Survival of the Biggest

#Write a program that receives a list of integer numbers (separated by a single space) and a number n. 
#The number n represents the count of numbers to remove from the list.
#You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

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
