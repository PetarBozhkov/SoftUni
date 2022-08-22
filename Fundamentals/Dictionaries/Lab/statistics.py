products = {}

command = input()
while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Product in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")




products_inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])

    if product not in products_inventory:
        products_inventory[product] = quantity
    else:
        products_inventory[product] += quantity

print("Products in stock:")
product_representation = [f"- {item}: {str(products_inventory[item])}" for item in products_inventory]
print('\n'.join(product_representation))
print(f"Total Products: {len(products_inventory)}")
print(f"Total Quantity: {sum(products_inventory.values())}")
