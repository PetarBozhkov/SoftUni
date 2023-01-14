#3. Fast Food
#You have a fast-food restaurant, and the food you are offering is previously prepared.
#Write a program that checks if you have enough food to serve lunch to all your customers. 
#You also want to know who the client with the biggest order for that day is.
#First, you will be given the quantity of the food you have for the day (an integer number). 
#Next, you will be given a sequence of integers (separated by a single space), each representing the quantity of food in each order. 
#Keep the orders in a queue.
#Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. 
#Before each order, check if you have enough food left to complete it:
#· If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
#· Otherwise, stop serving.

from collections import deque

food = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for order in orders.copy():
    if food - order >= 0:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders])}")
        break
else:
    print("Orders complete")
