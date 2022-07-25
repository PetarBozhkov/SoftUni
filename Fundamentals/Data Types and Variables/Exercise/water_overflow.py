#7. Water Overflow

#You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow. 
#On the following n lines, you will receive liters of water (integers), which you should pour into your tank.

#If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank

number_of_lines = int(input())
capacity = 255
water_counter = 0

for line in range(number_of_lines):
    liters_of_water = int(input())

    if capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue

    water_counter += liters_of_water
    capacity -= liters_of_water

print(water_counter)

