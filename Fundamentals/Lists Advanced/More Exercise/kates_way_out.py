#3. Kate's Way Out
#Kate is stuck in a maze. You should help her to find her way out.
#On the first line, you will be given how many rows there are in the maze. 
#On the following n lines, you will be given the maze itself. Here is a legend for the maze:
#· "#" - means a wall; Kate cannot go through there
#· " " - means empty space; Kate can go through there
#· "k" - the initial position of Kate; start looking for a way out from there
#There are two options: Kate either gets out or not:
#· If Kate can get out, print the following: "Kate got out in {number_of_moves} moves".
#Note: If there are two or more ways out, she always chooses the longest one.
#· Otherwise, print: "Kate cannot get out".

def remove_all_hashtag(matrix: list):
    for row in matrix:
        row = [i for i in row if i != '#']
    return matrix


number_of_row = int(input())
maze_rows = list()
for _ in range(number_of_row):
    maze_rows.append(list(map(str, input())))

for row in maze_rows:
    for index in range(len(row)):
        if row[index] == " ":
            row[index] = index

remove_all_hashtag(maze_rows)
print(maze_rows)
