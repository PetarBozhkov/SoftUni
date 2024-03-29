#4. Fashion Boutique
#You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. 
#On the following line, you will be given an integer representing the capacity for one rack in your store.
#You must arrange the clothes in the store and use the racks to hang up every piece of clothing. 
#You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. 
#Each piece of clothing has its value (an integer). 
#You must sum their values while you take them out of the box:
#· If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box).
#· If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
#In the end, print how many racks you have used to hang up the clothes.

clothes = [int(n) for n in input().split()]
rack_space = int(input())

racks_count = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()

    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = rack_space - cloth

print(racks_count)
