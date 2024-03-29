#2. Email Validator
#You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
#· NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
#· MustContainAtSymbolError - raise it when there is no "@" in the email
#· InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
#When an error is encountered, raise it with an appropriate message:
#· NameTooShortError - "Name must be more than 4 characters"
#· MustContainAtSymbolError - "Email must contain @"
#· InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
#Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
#If the current email is valid, print "Email is valid" and read the next one

from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4

pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = [".com", ".bg", ".net", ".org"]
email = input()

while email != "End":

    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError("Email should contain only one @!")
        if len(email.split("@")[0]) <= MIN_LENGTH:
            raise NameTooShortError(f"Name must be more than {MIN_LENGTH} characters")
        if findall(pattern_name, email)[0] != email.split("@")[0]:  # petar => ["petar", "abv.bg"] => [0] => "petar"
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots.")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    except IndexError:
        print("Invalid email!")

    else:
        print("Email is valid")

    email = input()
