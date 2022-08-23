#5. ASCII Values

#Write a program that receives a list of characters separated by ", ". 
#It should create a dictionary with each character as a key and its ASCII value as a value. 
#Try solving that problem using comprehension.

data = input().split(", ")
char_values = {key: ord(key) for key in data}
print(char_values)
