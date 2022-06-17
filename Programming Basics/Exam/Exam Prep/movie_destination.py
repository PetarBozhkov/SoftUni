budget = float(input())
destination = input()
season = input()
days = int(input())

total_sum = 0
if destination == "Dubai":
    if season == "Winter":
        total_sum = days * 45000
    elif season == "Summer":
        total_sum = days * 40000

    total_sum = total_sum * 0.70
elif destination == "Sofia":
    if season == "Winter":
        total_sum = days * 17000
    elif season == "Summer":
        total_sum = days * 12500

    total_sum = total_sum * 1.25
elif destination == "London":
    if season == "Winter":
        total_sum = days * 24000
    elif season == "Summer":
        total_sum = days * 20250

difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
