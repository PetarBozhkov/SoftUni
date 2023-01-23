#4. Parking Lot

#Write a program that:

#· Records a car number for every car that enters the parking lot

#· Removes a car number when the car leaves the parking lot

#On the first line, you will receive the number of commands - N. 
#On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". 
#The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. 
#Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".

#Note: The order in which we print the result does not matter.

def print_func(data):
    if data:
        for car_number in data:
            print(car_number)
    else:
        print('Parking Lot is Empty')
        

n = int(input())
plate_number_records = [input() for _ in range(n)]
parking_lot_data = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for record in plate_number_records:
    command, plate_number = record.split(', ')
    if command == COMMAND_IN:
        parking_lot_data.add(plate_number)
    elif command == COMMAND_OUT:
        parking_lot_data.remove(plate_number)
print_func(parking_lot_data)
