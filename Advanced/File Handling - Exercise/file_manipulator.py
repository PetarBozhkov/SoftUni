#3. File Manipulator
#Create a program that will receive commands until the command "End". The commands can be:
#· "Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
#· "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
#· "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string.If the file does not exist, print: "An error occurred"
#· "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

import os

while True:
    command, *info = input().split("-")  # Replace - some_file.txt - some text - not some text

    if command == "Create":
        file = open(f"files/{info[0]}", "w")
        file.close()
    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r") as file:
                text = file.read()
            text = text.replace(info[1], info[2])

            with open(f"files/{info[0]}", "w") as file:
                file.write(text)
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred!")

    elif command == "End":
        break
