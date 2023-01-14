#5. Truck Tour
#There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
#For each petrol pump, you will receive two pieces of information (separated by a single space):
#- The amount of petrol the petrol pump will give you
#- The distance from that petrol pump to the next petrol pump (kilometers)
#You are a truck driver, and you want to go all around the circle. 
#You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
#In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
#Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. 
#You never miss filling its tank at a petrol pump.

from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
index = 0
gas_in_tank = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank - distance < 0:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0
    else:
        gas_in_tank -= distance

print(index)
