toy = 5
jumper = 15
number_of_people = 0
number_of_kids = 0
number_of_adults = 0
money_for_toys = 0
money_for_jumpers = 0

command = input()

while command != "Christmas":
    number_of_people += 1
    if int(command) <= 16:
        number_of_kids += 1
        money_for_jumpers += toy
    else:
        number_of_adults += 1
        money_for_jumpers += jumper

    command = input()

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_jumpers}")

