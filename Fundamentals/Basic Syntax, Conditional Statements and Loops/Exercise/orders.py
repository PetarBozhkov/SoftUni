#5. Orders

#You work at a coffee shop, and your job is to place orders to the distributors. 
#Thus, you want to know the price of each order. 
#On the first line, you will receive integer N - the number of orders the shop will receive. 
#For each order, you will receive the following information:

#· Price per capsule - a floating-point number in the range [0.01…100.00]
#· Days - integer in the range [1…31]
#· Capsules, needed per day - integer in the range [1…2000]
#For each order, you should print a single line in the following format:
#· "The price for the coffee is: ${price}"
#If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and move to the next one.
#After you go through all orders, you need to print the total price in the following format:
#· "Total: ${total_price}"
#Both the price of a coffee and the total price must be formatted to the second decimal place.

number_of_orders = int(input())
total_price = 0

for oreder in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.0:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_per_day < 1 or needed_per_day > 2000:
        continue

    current_order_price = price_per_capsule * needed_per_day * days
    total_price += current_order_price

    print(f"The price for the coffee is: ${current_order_price:.2f}")

print(f"Total: ${total_price:.2f}")
