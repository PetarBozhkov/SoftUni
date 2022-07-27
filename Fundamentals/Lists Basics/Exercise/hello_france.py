#9. * Hello, France

#You want to go to France by train, and the train ticket costs exactly 150$. 
#You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.

#You will receive a collection of items and a budget in the following format:

#{type->price|type->price|type->price……|type->price}

#{budget}

#The prices for each of the types cannot exceed a specific price, which is given below:

#Type Maximum Price

#Clothes 50.00

#Shoes 35.00

#Accessories 20.50

#If a price for a particular item is higher than the maximum price, don't buy it. 
#Every time you buy an item, you have to reduce the budget with its price value. 
#If you don't have enough money for it, you can't buy it. Buy as many items as you can.

#Next, you should increase the price of each item you have successfully bought by 40% and then sell it. 
#Calculate if the budget after selling all the items is enough for buying the train ticket.

items_collections = input()
budget = float(input())

items_list = items_collections.split("|")

train_ticket = 150
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50

total_spend_money = 0
new_item_price_list = []

for item in items_list:
    current_items_list = item.split("->")

    if current_items_list[0] == "Clothes":
        if float(current_items_list[1]) <= clothes_max_price and float(current_items_list[1]) <= budget:
            budget -= float(current_items_list[1])
            total_spend_money += float(current_items_list[1])
            new_price = float(current_items_list[1]) * 1.4
            new_item_price_list.append(new_price)
        else:
            continue
    elif current_items_list[0] == "Shoes":
        if float(current_items_list[1]) <= shoes_max_price and float(current_items_list[1]) <= budget:
            budget -= float(current_items_list[1])
            total_spend_money += float(current_items_list[1])
            new_price = float(current_items_list[1]) * 1.4
            new_item_price_list.append(new_price)
        else:
            continue
    elif current_items_list[0] == "Accessories":
        if float(current_items_list[1]) <= accessories_max_price and float(current_items_list[1]) <= budget:
            budget -= float(current_items_list[1])
            total_spend_money += float(current_items_list[1])
            new_price = float(current_items_list[1]) * 1.4
            new_item_price_list.append(new_price)
        else:
            continue

profit = sum(new_item_price_list) - total_spend_money

a_new_item_price_list = [f"{num:.2f}" for num in new_item_price_list]
print(' '.join(map(str, a_new_item_price_list)))
print(f"Profit: {profit:.2f}")
if (budget + sum(new_item_price_list)) >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
