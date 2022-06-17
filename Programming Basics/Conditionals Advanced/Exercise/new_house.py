flower_type = input()
number_of_flowers = int(input())
budget = int(input())
flower_price = 0

if flower_type == "Roses" :
   flower_price = 5
   if number_of_flowers > 80:
    flower_price = 5 - (5 * 0.1)

if flower_type == "Dahlias":
   flower_price = 3.80
   if number_of_flowers > 90:
    flower_price = 3.80 - (3.80 * 0.15)

if flower_type == "Tulips":
    flower_price = 2.80
    if number_of_flowers > 80:
     flower_price = 2.80 - (2.80 * 0.15)

if flower_type == "Narcissus":
     flower_price = 3
     if number_of_flowers < 120:
      flower_price = 3 + (3 * 0.15)

if flower_type == "Gladiolus":
   flower_price = 2.50
   if number_of_flowers < 80:
     flower_price = 2.50 + (2.50 * 0.2)

total_price = number_of_flowers * flower_price
remaining_money = abs(total_price - budget)

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {remaining_money:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {remaining_money:.2f} leva more.")