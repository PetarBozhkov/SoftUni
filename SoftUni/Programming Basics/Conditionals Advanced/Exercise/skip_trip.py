movie_type = input()
rows = int(input())
columns = int(input())
cinema_capacity = rows * columns
price_per_ticket = 0

if movie_type == "Premier":
    price_per_ticket = 12
elif movie_type == "Normal":
    price_per_ticket == 7.5
elif movie_type == "Discount":
    price_per_ticket == 5

total_income = cinema_capacity * price_per_ticket
print(f"{total_income:.2f} leva")
