#1. Valid Usernames

#Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.

#A valid username:

#· has length between 3 and 16 characters inclusive

#· can contain only letters, numbers, hyphens, and underscores

#· has no redundant symbols before, after, or in between

data = input().split(", ")
usernames = list()
for user in data:
    if 3 <= len(user) <= 16 and (user.isalnum() or "-" in user or "_" in user):
        usernames.append(user)

for user in usernames:
    print(user)
