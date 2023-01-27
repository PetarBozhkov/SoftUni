#5. Santa's Present Factory
#This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
#First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. 
#After that, you will be given another sequence of integers – their magic level.
#Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
#Present Magic needed
#Doll 150
#Wooden train 250
#Teddy bear 300
#Bicycle 400
#You should take the last box with materials and the first magic level value to craft a toy. 
#Their multiplication calculates the total magic level. 
#If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. 
#Otherwise:
#· If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
#· If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
#· If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
#Stop crafting presents when you run out of boxes of materials or magic level values.
#Your task is considered done if you manage to craft either one of the pairs:
#· a doll and a train
#· a teddy bear and a bicycle

from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())
crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
    if not magic_level:
        continue

    product = material * magic_level
    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
