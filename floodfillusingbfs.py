from queue import Queue
import numpy as np
grid = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
])
def floodfillUsingBSF(img, row, col, p):
    start = img[row][col]

    queus = [(row, col)]

    visited = set()
    while not queus == []:
        row, col = queus.pop(0)
        visited.add((row, col))

        img[row][col] = p

        for row, col in neighbors(img, row, col,start):
            if(row, col) not in visited:
                queus.append((row, col))
    print(img)
    return img

def neighbors(img, row, col, start):
    indices = [(row -1, col), (row +1, col),(row, col-1),(row, col+1)]
    return [(row, col) for row, col in indices if isValid(img, row, col) and img[row][col] == start]
def isValid(img, row, col):
    return row >= 0 and col >= 0 and row<len(img) and col<len(img[0])
    

floodfillUsingBSF(grid,1,0,3)