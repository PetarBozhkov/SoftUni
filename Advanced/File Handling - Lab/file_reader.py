2. File Reader

You are given a file called numbers.txt with the following content:
    1 
    2 
    3 
    4 
    5

Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

file = open('./numbers.txt')
result = 0
for line in file:
    result += int(line)

print(result)
