#3. Statistics

#You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. 
#You have to accept all the new products coming in the bakery and finally gather some statistics.
#You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". 
#Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one. 
#When you receive the "statistics" command, print the following:

#"Products in stock:
#- {product1}: {quantity1}
#- {product2}: {quantity2}
#…
#- {productN}: {quantityN}

#Total Products: {count_all_products}
#Total Quantity: {sum_all_quantities}"

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
