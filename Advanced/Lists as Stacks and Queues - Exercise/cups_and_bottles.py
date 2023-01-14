#10. *Cups and Bottles
#You will be given a sequence of integers – each indicating a cup's capacity (in litters). 
#After that, you will be given another sequence of integers – each indicating a bottle's capacity (in litters). 
#Your job is to try to fill up all the cups.
#You must start picking from the last received bottle and start filling from the first entered cup. 
#You could pick exactly one bottle at a time. If the current bottle has N water, you give the first entered cup N water and reduce its integer value by N.
#When a cup's integer value reaches 0 or less, it gets removed. 
#It is possible that the current cup's value is greater than the current bottle's value. 
#In that case, you pick bottles until you reduce the cup's integer value to 0 or less. 
#If a bottle's value is greater or equal to the cup's current value, you fill up the cup, and the remaining water becomes wasted. 
#You should keep track of the wasted litters of water and print them at the end of the program.
#If you have managed to fill up all the cups, print the remaining water bottles, from the last entered – to the first. 
#Otherwise, you must print the remaining cups ordered by the entrance – from the first entered – to the last.

from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])
wasted_liters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_liters += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")
else:
    print(f"Bottles: {' '.join(str(bottle) for bottle in bottles)}")

print(f"Wasted litters of water: {wasted_liters}")
