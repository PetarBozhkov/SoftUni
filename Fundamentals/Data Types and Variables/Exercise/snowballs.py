#9. *Snowballs

#Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best snowballs. 
#They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.

#You will receive N – an integer, the number of snowballs being made by Tony and Andi. On the following lines, you will receive 3 inputs for each snowball:

#· The weight of the snowball (integer).

#· The time needed for the snowball to get to its target (integer).

#· The quality of the snowball (integer).

#For each snowball, you must calculate its value by the following formula:

#(snowball_weight / snowball_time) ** snowball_quality

#In the end, you must print the highest calculated value of a snowball

number_of_snowballs = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_snowball_value = 0

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball_value = (weight_of_the_snowball / time_needed) ** quality
    if current_snowball_value > max_snowball_value:
        max_snowball_weight = weight_of_the_snowball
        max_snowball_time = time_needed
        max_snowball_value = current_snowball_value

print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")

