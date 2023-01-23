#3. Record Unique Names

#Write a program, which will take a list of names and print only the unique names in the list.

#The order in which we print the result does not matter

n = int(input())
names_data = {input() for _ in range(n)}

for name in names_data:
    print(name)
