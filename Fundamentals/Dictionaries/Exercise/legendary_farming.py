#5. Legendary Farming

#You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. 
#However, it's a tedious process, and it requires quite a bit of farming. The possible items are:

#· "Shadowmourne" - requires 250 Shards
#· "Valanyr" - requires 250 Fragments
#· "Dragonwrath" - requires 250 Motes
#"Shards", "Fragments", and "Motes" are the key materials (case-insensitive), and everything else is junk.

#You will be given lines of input in the format:
#"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"

#Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.

#In the end, print the remaining shards, fragments, motes in the format:

#"shards: {number_of_shards}
#fragments: {number_of_fragments}
#motes: {number_of_motes}"

#Finally, print the collected junk items in the order of appearance.

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while not obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in items.keys(): #in useless_items
                items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()
for material,quantity in items.items():
    print(f"{material}: {quantity}")
