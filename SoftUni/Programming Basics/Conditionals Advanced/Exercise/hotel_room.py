month = input()
number_of_nights = int(input())
type_of_room = ""
room_price = 0
price = room_price * number_of_nights

if month == "May" or month == "October":
 room_price = 50 and type_of_room == "Studio"
 print(f"Studio: {price:.2f} lv.")

 if month == "May" or month == "October":
       room_price = 65 and type_of_room == "Apartment"
       print(f"Aparment: {price:.2f} lv.")

if month == "June" or month == "September":
 room_price = 75.20 and type_of_room == "Studio"
else:
 room_price = 68.70 and type_of_room == "Apartment"

if month == "July" or month == "August":
    room_price = 76 and type_of_room == "Studio"
else:
    room_price = 77 and type_of_room == "Apartment"

if number_of_nights > 7 and month == "May" or month == "October":
        price *= 0.95 and type_of_room == "Studio"
elif number_of_nights > 14 and month == "May" or month == "October":
    price *= 0.70 and type_of_room == "Studio"

if number_of_nights > 14 and month == "June" or month == "September":
    price *= 0.80 and type_of_room == "Studio"

if number_of_nights > 14:
    price *= 0.90





