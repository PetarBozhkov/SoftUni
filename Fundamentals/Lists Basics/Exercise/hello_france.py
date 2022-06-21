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
