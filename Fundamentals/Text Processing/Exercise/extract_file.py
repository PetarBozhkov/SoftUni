#3. Extract File

#Write a program that reads the path to a file and subtracts the file name and its extension.

file_path = input().split("\\")
file_name = file_path[-1].split(".")[0]
file_extension = file_path[-1].split(".")[-1]
print(f"File name: {file_name}\nFile extension: {file_extension}")
