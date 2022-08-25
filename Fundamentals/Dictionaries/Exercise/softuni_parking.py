#7. SoftUni Parking

#SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. 
#Good thing you're on the dev team and know how to fix it, right?

#Write a program, which validates a parking place - users can register to enter the park and unregister to leave.

#The program receives 2 types of commands:

#· "register {username} {license_plate_number}":

#o The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print: "ERROR: already registered with plate number {license_plate_number}"

#o If the check above passes successfully, the user should be registered, so the system should print: "{username} registered {license_plate_number} successfully"

#· "unregister {username}":

#o If the user is not present in the database, the system should print: "ERROR: user {username} not found"

#o If the check above passes successfully, the system should print: "{username} unregistered successfully"

#After you execute all of the commands, print all the currently registered users and their license plates in the format:

#· "{username} => {license_plate_number}"

count_command = int(input())
softuni_parking = dict()
for i in range(count_command):
    commands = input().split(" ")
    command, username = commands[0], commands[1]
    if command == "register":
        license_plate_number = commands[2]
        if username not in softuni_parking.keys():
            softuni_parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command == "unregister":
        if username not in softuni_parking.keys():
            print(F"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            softuni_parking.pop(username)

for username, license_plate_number in softuni_parking.items():
    print(f"{username} => {license_plate_number}")
