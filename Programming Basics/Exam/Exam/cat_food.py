number_of_cats = int(input())
grams_food = float(input())
one_kg_food = 12.45
small_cats = 0
big_cats = 0
huge_cats = 0

for number in range(number_of_cats + 1):
    current_number = int(input())
    if 100 >= grams_food < 200:
        small_cats += 1
    elif 200 >= grams_food < 300:
        big_cats += 1
    elif 300 >= grams_food < 400:
        huge_cats += 1
    sum += current_number







