#7. *Robotics
#There is a robotics factory. The current project is assembly-line robots.
#Each robot has a processing time – it is the time in seconds the robot needs to process a product. 
#When a robot is free, it should take a product for processing and log its name, product, and processing start time.
#Each robot processes a product coming from the assembly line. 
#A product is coming from the line each second (so the first product should appear at [start time + 1 second]). 
#If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
#The robots are standing in the line in the order of their appearance.

from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}  # {name: [time_needed, time_for_curr_task]
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
