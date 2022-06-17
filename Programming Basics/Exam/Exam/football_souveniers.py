team = input()
type_of_souvenier = input()
number_of_souveniers = int(input())
price = 0

if team == "Argentina":
    if type_of_souvenier == "flags":
        price = 3.25
    elif type_of_souvenier == "caps":
         price = 7.20
    elif type_of_souvenier == "posters":
        price = 5.10
    elif type_of_souvenier == "stickers":
        price = 1.25
elif team == "Brazil":
    if type_of_souvenier == "flags":
        price = 4.20
    elif type_of_souvenier == "caps":
         price = 8.50
    elif type_of_souvenier == "posters":
        price = 5.35
    elif type_of_souvenier == "stickers":
        price = 1.20
elif team == "Croatia":
    if type_of_souvenier == "flags":
        price = 2.75
    elif type_of_souvenier == "caps":
         price = 6.90
    elif type_of_souvenier == "posters":
        price = 4.95
    elif type_of_souvenier == "stickers":
        price = 1.10
elif team == "Denmark":
    if type_of_souvenier == "flags":
        price = 3.10
    elif type_of_souvenier == "caps":
         price = 6.50
    elif type_of_souvenier == "posters":
        price = 4.80
    elif type_of_souvenier == "stickers":
        price = 0.90

final_price = price * number_of_souveniers

if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if type_of_souvenier == "flags" or type_of_souvenier == "caps" or type_of_souvenier == "posters" or type_of_souvenier == "stickers":
        print(f"Pepi bought {number_of_souveniers} {type_of_souvenier} of {team} for {final_price:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")