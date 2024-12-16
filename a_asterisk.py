from pyamaze import maze, agent
from queue import PriorityQueue
import math
import time
GOAL = (1, 1)

# Define H-function
# Manhattan distance
def h1(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

# Euclidean distance
def h2(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def aStar(m, h):
    # Start position (0,0 corner)
    start = (m.rows, m.cols)
    # Cost from starting point to cell, Initialize all cell as infinity
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = g_score[start] + h(start, GOAL)
    
    pqueue = PriorityQueue()
    # Priority Queue Store a tuple with f score, heuristic function, and cell
    pqueue.put((f_score[start], h(start, GOAL), start))
    
    a_path = {}
    
    while not pqueue.empty():
        currCell = pqueue.get()[2]
        
        if currCell == GOAL:
            break
        
        for direction in 'ESNW':
            if m.maze_map[currCell][direction] == 1:
                # Neighbor Cell is on right hand side
                if direction == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if direction == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if direction == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if direction == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                
                new_g_score = g_score[currCell] + 1
                new_f_score = new_g_score + h(childCell, GOAL)

                if new_f_score < f_score[childCell]:
                    g_score[childCell] = new_g_score
                    f_score[childCell] = new_f_score
                    pqueue.put((new_f_score, h(childCell, GOAL), childCell))
                    a_path[childCell] = currCell
    
    # Reconstruct the path from goal to start
    ans_path = {}
    cell = GOAL
    while cell != start:
        ans_path[a_path[cell]] = cell
        cell = a_path[cell]
    
    return ans_path


# Create matrix with n size from pyamaze
m = maze(5, 5)
print(m.cols)
m.CreateMaze()
a = agent(m, footprints= True)
path = aStar(m, h1)
time.sleep(1)
m.tracePath({a:path})

# Present UI
m.run()



