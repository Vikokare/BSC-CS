import pandas as pd

maze = [
    ['A', ' ', ' ', ' ', ' '],
    ['*', ' ', '*', '*', ' '],
    ['*', ' ', ' ', '*', ' '],
    ['*', '*', ' ', '*', ' '],
    ['*', '*', ' ', ' ', 'B']
]
print(pd.DataFrame(maze))

# Handle out of range index
# handle multiple path

def get_current_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if 'A' == maze[i][j]:
                print(maze[i][j], i, j)
                return i, j


def route(maze, current_index):

    count = 1
    while True:

        row, col = current_index
        print(row, col)
        
        if (row > 0 and maze[row - 1][col] == 'B') or (row < 4 and maze[row + 1][col] == 'B') or (col > 0 and maze[row][col - 1] == 'B') or (col < 4 and maze[row][col + 1] == 'B'):
            print("You escaped my clutches, Lucky Bastard...")
            break

        
        # Moving Up
        if row > 0 and maze[row - 1][col] == ' ':
            print("Moving Up")
            maze[row][col], maze[row - 1][col] = count, maze[row][col]
            current_index = row - 1, col

        # Moving Down
        elif row < 4 and maze[row + 1][col] == ' ':
            print("Moving Down")
            maze[row][col], maze[row + 1][col] = count, maze[row][col]
            current_index = row + 1, col

        # Moving Left
        elif col > 0 and maze[row][col - 1] == ' ':
            print("Moving Left")
            maze[row][col], maze[row][col - 1] = count, maze[row][col]
            current_index = row, col - 1

        # Moving Right
        elif col < 4 and maze[row][col + 1] == ' ':
            print("Moving Right")
            maze[row][col], maze[row][col + 1] = count, maze[row][col]
            current_index = row, col + 1

        else:
            print("You are stuck forever :(")
            break

        count = count + 1

    print(pd.DataFrame(maze))

current_index = get_current_position(maze)

route(maze, current_index)


