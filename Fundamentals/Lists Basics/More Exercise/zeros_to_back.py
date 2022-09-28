#1. Zeros to Back
#Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and moves them to the back without messing up the other elements. 
#Print the resulting integer list.

the_string = input().replace(', ',' ').split()
the_list = []
count = 0
for i in the_string:
    if i == '0':
        count += 1
    else:
        the_list.append(int(i))
for i in range(count):
    the_list.append(0)
print(the_list)
