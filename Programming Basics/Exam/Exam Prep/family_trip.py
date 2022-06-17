budget = float(input())
count_nights = int(input())
price_night = float(input())
percent_expenses = int(input())

if count_nights > 7:
    price_night = price_night * 0.95

all_nights_sum = count_nights * price_night
expenses = budget * (percent_expenses / 100)
total_price = all_nights_sum + expenses
difference = abs(total_price - budget)

if budget >= total_price:
  print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
