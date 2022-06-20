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

