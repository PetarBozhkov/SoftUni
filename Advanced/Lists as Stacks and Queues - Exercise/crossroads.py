#8. *Crossroads
#The super-spy action hero Sam has finally found some time to go on a holiday. 
#He is taking his wife somewhere nice, and they're going to have a really good time, but first, they have to get there. 
#Even on his holiday trip, Sam is still going to run into some problems, and the first one is getting to the airport. 
#Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
#Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely.
#Sam is on a single lane of cars that queue until the light goes green. 
#When it does, they start passing one by one on a flashing green light and during the free window before the intersecting road's light goes green. 
#For each second, only one part of a car (a single character) passes the crossroad. 
#If a car is still in the middle of the crossroads when the free window ends, it will get hit at the first character that is still in the crossroads.

from collections import deque

green_window = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
info = input()

while info != "END":
    if info != "green":
        cars.append(info)
    else:
        current_green = green_window

        while current_green > 0 and cars:
            car = cars.popleft()

            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

    info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
