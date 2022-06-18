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