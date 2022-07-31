#2. The Lift Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2517#1.

#Write a program that finds a place for the tourist on a lift.

#Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one with space available.

def lift_func(waiting_people, current_state_of_the_lift):
    for i in range(len(current_state_of_the_lift)):
        if waiting_people > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
            waiting_people -= current_number_of_people
            current_state_of_the_lift[i] += current_number_of_people
        else:
            current_state_of_the_lift[i] += waiting_people
            waiting_people = 0
    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print(f"The lift has empty spots!")
    return ' '.join([str(num) for num in current_state_of_the_lift])


number_of_people = int(input())
lift_condition = list(map(int, input().split(' ')))
print(lift_func(number_of_people, lift_condition))
