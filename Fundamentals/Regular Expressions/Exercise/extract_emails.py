#4. Extract Emails

#Write a program that receives a single string and extracts all email addresses from it. Print the extracted email addresses on separate lines. 
#Emails are in the format "{user}@{host}", where:

#· {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
#o Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
#o Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
#· {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".". 

#Each word consists of only letters and can have hyphens "-" between the letters.

#o Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
#o Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"

import re

user_input = input()
user_name_patter = r"( |^)[a-zA-Z0-9]+((([\._-])[a-zA-Z0-9]+)*)*"
email_patter = r"[a-zA-Z0-9]+([\-]\w+)*\.[a-zA-Z0-9]+((\.\w+)*)*\b"
matches_email = re.finditer(fr"{user_name_patter}@{email_patter}", user_input)
emails = list()
for match in matches_email:
    emails.append(match.group())
print("\n".join(emails))
