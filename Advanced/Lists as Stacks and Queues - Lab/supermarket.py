#3. Supermarket

#Tom is working at the supermarket, and he needs your help to keep track of his clients. 
#Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. 
#If, in the meantime, you receive the command "Paid", you should print each customer in the order they are served (from the first to the last one) and empty the queue.

#When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining.".

from _collections import deque

names_deque = deque()
COMMAND_END = 'End'
COMMAND_PAID = 'Paid'

while True:
    command = input()

    if command == COMMAND_END:
        print(f'{len(names_deque)} people remaining.')
        break

    elif command == COMMAND_PAID:
        while names_deque:
            print(names_deque.popleft())

    else:
        names_deque.append(command)
