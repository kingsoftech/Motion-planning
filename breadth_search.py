import numpy as np
from enum import Enum
from queue import Queue
grid = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
])
start = (0, 0)
goal = (1, 4)
class Action(Enum):
    LEFT  = (0, -1)
    RIGHT = (0, 1)
    UP    = (-1, 0)
    DOWN  = (1, 0)

    def __str__(self) -> str:
        if(self == self.LEFT):
            return '<'
        if(self == self.RIGHT):
            return '>'
        elif(self ==self.UP):
            return '^'
        elif(self == self.DOWN):
            return 'v'
        return super().__str__()
    
def valid_actions(grid, current_node):
    """
    Returns a list of valid actions given a grid and current node.
    """
    # First define a list of all possible actions
    valid = [Action.UP, Action.LEFT, Action.RIGHT, Action.DOWN]
    # Retrieve the grid shape and position of the current node
    n, m = grid.shape[0] - 1, grid.shape[1] - 1
    x, y = current_node
    
    # check if the node is off the grid or it's an obstacle
    # If it is either, remove the action that takes you there
    
    #helps keeps the boundaries in check and the blocked paths 
    if x - 1 < 0 or grid[x-1, y] == 1:
        valid.remove(Action.UP)
    if x + 1 > n or grid[x+1, y] == 1:
        valid.remove(Action.DOWN)
    if y - 1 < 0 or grid[x, y-1] == 1:
        valid.remove(Action.LEFT)
    if y + 1 > m or grid[x, y+1] == 1:
        valid.remove(Action.RIGHT)
        
    return valid

# Define a function to visualize the path
def visualize_path(grid, path, start):
    """
    Given a grid, path and start position
    return visual of the path to the goal.
    
    'S' -> start 
    'G' -> goal
    'O' -> obstacle
    ' ' -> empty
    """
    # Define a grid of string characters for visualization
    sgrid = np.zeros(np.shape(grid), 'U1')
    sgrid[:] = ' '
    sgrid[grid[:] == 1] = 'O'
    
    pos = start
    # Fill in the string grid
    for a in path:
        da = a.value
        sgrid[pos[0], pos[1]] = str(a)
        pos = (pos[0] + da[0], pos[1] + da[1])
    sgrid[pos[0], pos[1]] = 'G'
    sgrid[start[0], start[1]] = 'S'  
    return sgrid
def dfs(grid,start, goal):
    stack = [start]

    visited = set()
    visited.add(start)

    branch ={}
    valid_movement = []
    found = False
    while len(stack) > 0:
        current_node =  stack.pop()
        
        if current_node == goal:
            found = True
            print("found a path ")
            break
        else:
            
            for a in valid_actions(grid, current_node):
                available_action = a.value
                #print(a)
                valid_movement.append(a)
                # getting the value of next node through the available actions
                next_node = (current_node[0] + available_action[0], current_node[1] + available_action[1])
                if next_node not in visited:
                    visited.add(next_node)
                    stack.append(next_node)
                    branch[next_node] = (current_node, a)
    path = []
    if found:
        path = []
        n= goal
        while branch[n][0] != start:
            path.append(branch[n][1])
            n = branch[n][0]
        path.append(branch[n][1])

    print(valid_movement)
    return path[::-1]

def bfs(grid, start, goal):

    queue = Queue()
    queue.put(start)

    visited = set()
    visited.add(start)

    branch = {}
    found = False
    while not queue.empty():
        #setting the current_node to the correct state of the queue which is start state
        current_node = queue.get()
        if current_node == goal:
            print("found a path")
            found = True
            break
        else:
           
            #iterate to check the valid action for the current node
            for a in valid_actions(grid,  current_node):
                #getting the value of a because a value is inform of (1,0)
                available_action = a.value
                # getting the value of next node through the available actions
                next_node = (current_node[0] + available_action[0], current_node[1] + available_action[1]) 
                if(next_node not in visited):
                    visited.add(next_node)
                    queue.put(next_node)
                    branch[next_node] = (current_node, a)
        
    path = []
    if found:
        path = []
        n= goal
        while branch[n][0] != start:
            path.append(branch[n][1])
            n = branch[n][0]
        path.append(branch[n][1])


    return path[::-1]


path = dfs(grid, start, goal)
start = (0, 0)
goal = (2, 2)
print(visualize_path(grid, path, start))
