#3. Wolf in Sheep's Clothing
#Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be sheep. 
#Fortunately, you are good at spotting them.
#Warn the sheep in front of the wolf that it is about to be eaten. 
#Remember that you are standing at the front of the queue, which is at the end of the list:

#[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#4 3 2 1

#If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
#Note: there will always be exactly one wolf on the list.

animals = input()
all_animals = animals.split(', ')
all_animals.reverse()
count = 0

for animal in all_animals:
    if animal != 'wolf':
        count += 1
    if animal == 'wolf':
        break
if count == 0:
    print(f'Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {count}! You are about to be eaten by a wolf!')
