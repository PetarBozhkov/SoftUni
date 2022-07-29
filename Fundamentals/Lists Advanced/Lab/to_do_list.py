#3. To-do List

#You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
#Return a list containing all to-do notes sorted by importance in ascending order.
#The importance value will always be an integer between 1 and 10 (inclusive).

#Hint
#· Use the pop() and insert() methods.

tasks = []

while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    priority = int(command[0])
    task = command[1]
    tasks.append((priority, task))

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
