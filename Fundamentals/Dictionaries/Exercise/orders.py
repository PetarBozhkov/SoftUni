#6. Orders

#Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:

#· If the product doesn't exist yet, add it with its starting quantity.

#· If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.

#You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. 
#Finally, print all items with their names and the total price of each product.

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

