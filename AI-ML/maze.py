import heapq
import pandas as pd

maze = [
    ['A', '*', ' ', ' ', 'B'],
    [' ', ' ', ' ', '*', '*'],
    [' ', ' ', ' ', '*', '*'],
    [' ', '*', ' ', '*', '*'],
    [' ', ' ', ' ', '*', '*']
]
print(pd.DataFrame(maze))

# Heuristic function (Manhattan Distance)
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# Find the position of 'A' and 'B'
def find_position(maze, symbol):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == symbol:
                return (i, j)


# A* algorithm
def a_star(maze, start, goal):
    heap_list = []
    heapq.heappush(heap_list, (0, start))
    traces = {}
    g_score = {start: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap_list:
        current_f, current_pos = heapq.heappop(heap_list)
        row, col = current_pos

        if current_pos == goal:
            print("Goal Reached!")
            reconstruct_path(maze, traces, current_pos)
            return
        
        for d in directions:
            neighbor_pos = (neighbor_row, neighbor_col) = row + d[0], col + d[1]
            
            if 0 <= neighbor_row <= len(maze) and 0 <= neighbor_col <= len(maze) and maze[neighbor_row][neighbor_col] != '*':
                tentative_g_score = g_score[current_pos] + 1

                if neighbor_pos not in g_score or tentative_g_score < g_score[neighbor_pos]:
                    g_score[neighbor_pos] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor_pos, goal)
                    heapq.heappush(heap_list, (f_score, neighbor_pos))
                    traces[neighbor_pos] = current_pos


def reconstruct_path(maze, traces, current_pos):
    while current_pos in traces:
        current_pos = traces[current_pos]
        maze[current_pos[0]][current_pos[1]] = '•'
    maze[current_pos[0]][current_pos[1]] = 'A'
    print(pd.DataFrame(maze))


a_star(maze, find_position(maze, 'A'), find_position(maze, 'B'))