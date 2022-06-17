series_title = input()
episode_duration = int(input())
break_duration = int(input())
lunch_time = break_duration * 1/8
break_time = break_duration * 1/4

remaining_time = abs(break_duration - lunch_time - break_time)
time_left = abs(remaining_time - episode_duration)

if remaining_time >= episode_duration:
    print(f"You have enough time to watch {series_title} and left with {time_left.__ceil__()} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_title}, you need {time_left.__ceil__()} more minutes.")
