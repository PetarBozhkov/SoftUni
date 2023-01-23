#5. SoftUni Party
#There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. 
#When a guest comes, check if they exist on any of the two reservation lists.
#On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their reservation codes. 
#All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
#After that, you will be receiving guests who came to the party until you read the "END" command.
#In the end, print the number of guests who did not come to the party and their reservation numbers:
#· The VIP guests must be first.
#· Both the VIP and the Regular guests must be sorted in ascending order.

def collect_data_for_arrived_guests():
    arrived_guests_list = []
    while True:
        data = input()
        if data == 'END':
            break
        else:
            arrived_guests_list.append(data)
    return arrived_guests_list


def print_func(not_arrived_guests_data):
    print(len(not_arrived_guests_data))
    for guest_number in sorted(not_arrived_guests_data):
        print(guest_number)


n = int(input())
guest_reservation_list = [input() for _ in range(n)]
arrived_guests = collect_data_for_arrived_guests()
not_arrived_guests = set(guest_reservation_list).difference(arrived_guests)
print_func(not_arrived_guests)
