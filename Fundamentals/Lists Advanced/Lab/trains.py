#2. Trains

#You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:

#· "add {people}" – you should add the number of people in the last wagon

#· "insert {index} {people}" - you should add the number of people at the given wagon

#· "leave {index} {people}" - you should remove the number of people from the wagon. 
#There will be no case in which the people will be more than the count in the wagon.

#There will be no case in which the index is invalid!

#After you receive the "End" command print the train.

number = int(input())
wagons = [0] * number

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(' ')
    current_command = data[0]

    if current_command == 'add':
        people_to_add = data[1]
        wagons[-1] += int(people_to_add)

    elif current_command == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people

    elif current_command == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people

print(wagons)
