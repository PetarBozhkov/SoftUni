#5. Furniture

#Write a program that calculates the total cost of bought furniture.
#You will be given information about each purchase on separate lines until you receive the command "Purchase". 
#Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. 
#You should store the names of the furniture and the total price.
#In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:

#"Bought furniture:

#{1st name}

#{2nd name}

#…

#{N name}

#Total money spend: {total_cost}"

import re

product_info = input()
total_amount = 0
furniture_name = list()
expression = r"\>{2}(?P<product_name>\w+)\<{2}(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"

while product_info !="Purchase":
    matches_product = re.finditer(expression, product_info)
    for match in matches_product:
        product_name = match.group("product_name")
        price = match.group("price")
        if "." in price:
            price.replace(".", ",")
        quantity = match.group("quantity")
        furniture_name.append(product_name)
        total_amount += float(price) * int(quantity)
    product_info = input()
print("Bought furniture:")

for furniture in furniture_name:
    print(furniture)
print(f"Total money spend: {total_amount:.2f}")
