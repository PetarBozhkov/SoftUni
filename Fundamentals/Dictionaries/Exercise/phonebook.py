#4. Phonebook

#Write a program that receives info from the console about people and their phone numbers.

#Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.

#After filling the phonebook, you will receive a number – N. 
#Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}". 
#In case the contact isn't found, print: "Contact {name} does not exist."

phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    name, phone = entry.split("-")
    phone_book[name] = phone
for checking in range(int(entry)):
    searched_contact = input()
    if searched_contact in phone_book.keys(): # in phone_book
        print(f"{searched_contact} -> {phone_book[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
