#5. Tic-Tac-Toe
#You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
#Legend:
#· 0 - empty space
#· 1 - first player move
#· 2 - second player move
#Find out who the winner is. If the first player wins, print "First player won". 
#If the second player wins, print "Second player won". Otherwise, print "Draw!".

def is_first_win(first_move: list, second_move: list, third_move: list):
    if first_move.count('1') == 3 or second_move.count('1') == 3 or third_move.count('1') == 3:
        return True
    elif first_move[0] == '1':
        if second_move[1] == '1' and third_move[2] == '1':
            return True
        elif second_move[0] == '1' and third_move[0] == '1':
            return True
    elif first_move[1] == '1':
        if second_move[1] == '1' and third_move[1] == '1':
            return True
    elif first_move[2] == '1':
        if second_move[1] == '1' and third_move[0] == '1':
            return True
        elif second_move[2] == '1' and third_move[2] == '1':
            return True
        

def is_second_win(first_move: list, second_move: list, third_move: list):
    if first_move.count('2') == 3 or second_move.count('2') == 3 or third_move.count('2') == 3:
        return True
    elif first_move[0] == '2':
        if second_move[1] == '2' and third_move[2] == '2':
            return True
        elif second_move[0] == '2' and third_move[0] == '2':
            return True
    elif first_move[1] == '2':
        if second_move[1] == '2' and third_move[1] == '2':
            return True
    elif first_move[2] == '2':
        if second_move[1] == '2' and third_move[0] == '2':
            return True
        elif second_move[2] == '2' and third_move[2] == '2':
            return True


first_move = input().split(' ')
second_move = input().split(' ')
third_move = input().split(' ')
if bool(is_first_win(first_move=first_move, second_move=second_move, third_move=third_move)):
    print('First player won')
elif bool(is_second_win(first_move=first_move, second_move=second_move, third_move=third_move)):
    print('Second player won')
else:
    print('Draw!')
