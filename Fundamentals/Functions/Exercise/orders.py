#5. Orders

#Write a function that calculates the total price of an order and returns it. 
#The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. 
#The prices for a single piece of each product are:

#· coffee - 1.50

#· water - 1.00

#· coke - 1.40

#· snacks - 2.00

#Print the result formatted to the second decimal place.

def orders_func(product: str, quantity: int):
    price = 0
    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1.00
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2.00
    return f'{price * quantity:.2f}'


type_of_product = input()
product_quantity = int(input())
print(orders_func(type_of_product, product_quantity))

# my solution
# product = input()
# quantity = int(input())
# coffee = 1.50
# water = 1.00
# coke = 1.40
# snacks = 2.00
# final_price = 0
# if product == 'coffee':
#     final_price = coffee * quantity
# elif product == 'water':
#     final_price = water * quantity
# elif product == 'coke':
#     final_price = coke * quantity
# elif product == 'snacks':
#     final_price = snacks * quantity
# print(f'{final_price:.2f}')
