products_dict = {}

while True:
    command = input()
    if command == "buy":
        break
    product = command.split(" ")
    name = product[0]
    price = float(product[1])
    quantity = int(product[2])
    if name not in products_dict:
        products_dict[name] = [price, quantity]
    else:
        products_dict[name][1] += quantity
        if products_dict[name][0] != price:
            products_dict[name][0] = price

for key, value in products_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

