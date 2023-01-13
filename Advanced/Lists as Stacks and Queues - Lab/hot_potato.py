#5. Hot Potato
#Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. 
#Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.
#Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. 
#On the second line, you will receive the nth toss (integer) in which a child leaves the game.
#Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".

from _collections import deque

name_of_players = input().split(' ')
step_of_hot_potato = int(input())
players_deque = deque(name_of_players)


while len(players_deque) > 1:
    for _ in range(step_of_hot_potato - 1):
        players_deque.append(players_deque.popleft())

    print(f'Removed {players_deque.popleft()}')

print(f'Last is {players_deque.pop()}')
