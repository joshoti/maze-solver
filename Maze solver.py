""" Maze Solver """
class Cell:
    def __init__(self, index):
        self.location = index
        self.borderLeft = False
        self.borderRight = False
        self.borderUp = False
        self.borderDown = False

    def neighbours(self):
        """
        Returns List of neighbours of current cell

        Variables        
            neighbourMapping(list): maps index to border location that we check
            l(int): index of left neighbour
            r(int): right neighbour. and so on
            neighbourMapping (0 -> left) (1 -> right) (2 -> down) (3 -> up)

        Explanation
            If we are in location 2, left neighbour(location) = 1
            and f"maze[{Row}][{Col}].{neighbourMapping[{index}]}" for Left, results to
            "maze[0][0].borderRight"
        """
        neighbourArray = []
        neighbourMapping = ['borderRight', 'borderLeft', 'borderUp', 'borderDown']
        l = self.location-1
        r = self.location+1
        d = self.location+n
        u = self.location-n
                
        for index, i in enumerate([l,r,d,u]):
            if index < 2: # L & R
                if (i-1)//n != (self.location-1)//n: # If not in same grid row
                    continue
            else: # D & U
                if not(1 <= i <= n*n): # If vertically out of bounds
                    continue
            Row,Col = IndexToGrid(i)
            border = neighbourMapping[index]
            neighbourArray.append(f"maze[{Row}][{Col}].{border}")
        return neighbourArray
	    
def makeMaze(puzzle):
    import numpy as np
    global n
    puzzlePicker = {1: [3, fillMaze1], 2: [3, fillMaze2], 3: [8, fillMaze3]}    
    n, fillFunction = puzzlePicker[puzzle]    
    maze = np.zeros((n,n), dtype=object) # Create grid
    i = 1
    for row in range(n):
        for col in range(n):
            maze[row][col] = Cell(i) # Make Cell object
            i += 1
    return fillFunction(maze) # Add borders

def insertBorder(index, string, maze):
    """
    Parameters
        index(int): location of cell to modify
        string(str): letters representing border to activate
        maze(2D array)

    Example Use
        >>> insertBorder(1, 'lrd')
        maze[0][0].borderLeft = True
        maze[0][0].borderRight = True
        maze[0][0].borderDown = True
    """
    Row, Col = IndexToGrid(index)
    for letter in string:
        if letter.lower() == 'l':
            maze[Row][Col].borderLeft = True
        elif letter.lower() == 'r':
            maze[Row][Col].borderRight = True
        elif letter.lower() == 'u':
            maze[Row][Col].borderUp = True
        elif letter.lower() == 'd':
            maze[Row][Col].borderDown = True

def fillMaze1(maze):
    """
    MAZE DIAGRAM (n = 3)
    A = 1, B = 3 (finish)
    ______ ___         _ _ _ 
   | A  __| B |       |A _|B|   
   |   |__    |       | |_  |
   |__________|       |_ _ _|
    """    
    insertBorder(2, 'rd', maze)
    insertBorder(3, 'r', maze)
    insertBorder(4, 'r', maze)
    insertBorder(8, 'u', maze)
    return maze

def fillMaze2(maze):
    """
    MAZE DIAGRAM (n = 3)
    A = 1, B = 3 (finish)
    ______ ___        _ _ _ 
   | A  __| B |      |A _|B|    
   |   |__    |      | |_  |
   |______|___|      |_ _|_|
    """
    insertBorder(1, 'lu', maze)
    insertBorder(2, 'urd', maze)
    insertBorder(3, 'ur', maze)
    insertBorder(4, 'lr', maze)
    insertBorder(6, 'r', maze)
    insertBorder(8, 'ur', maze) # difference: separates the left and right half
    insertBorder(9, 'dr', maze)
    return maze

def fillMaze3(maze):
    """
    MAZE DIAGRAM (n = 8)
    A = 1, B = 32, C = 33, F = 30 (Finish)
    _ _ _ _ _ _ _ _ 
   |A _ _ _|  _ _  |
   |_| |  _  |   | |
   |   |_  | | |_ _|
   | | |  _|_|F|  B|
   |C| |_  |_ _| | |
   |_| |  _  |_ _| |
   | |_ _|  _ _|  _|
   |_ _ _ _|_ _ _ _|
    """
    insertBorder(4, 'dr', maze)
    insertBorder(9, 'dr', maze)
    insertBorder(10, 'u', maze)
    insertBorder(11, 'ul', maze)
    insertBorder(12, 'd', maze)
    insertBorder(14, 'ul', maze)
    insertBorder(15, 'ur', maze)
    insertBorder(18, 'r', maze)
    insertBorder(19, 'd', maze)
    insertBorder(21, 'lr', maze)
    insertBorder(23, 'ld', maze)
    insertBorder(24, 'd', maze)
    insertBorder(26, 'lr', maze)
    insertBorder(28, 'dr', maze)
    insertBorder(29, 'dr', maze)
    insertBorder(31, 'l', maze)
    insertBorder(33, 'dr', maze)
    insertBorder(35, 'ld', maze)
    insertBorder(37, 'ld', maze)
    insertBorder(38, 'dr', maze)
    insertBorder(39, 'r', maze)
    insertBorder(42, 'lr', maze)
    insertBorder(46, 'ld', maze)
    insertBorder(47, 'dr', maze)
    insertBorder(50, 'ld', maze)
    insertBorder(51, 'd', maze)
    insertBorder(52, 'ul', maze)
    insertBorder(54, 'dr', maze)
    insertBorder(61, 'lu', maze)
    insertBorder(64, 'u', maze)
    return maze

def IndexToGrid(index):
    """
    Uses index to calculate the grid coordinates

    Example Use
        n = 3
        >>> IndexToGrid(1) # index 1 in a 3x3 grid
        (0,0)

        >>> IndexToGrid(8) # index 8 in a 3x3 grid
        (2,1)
    """
    return (index-1)//n, (index-1)%n # (row, col)

def MakeSet(n):
    """
    Creates 2 Arrays
    
    See Algorithms.py (Disjoint Set) for full documentation
    """
    ParentArray = [0]*n
    RateArray = ParentArray.copy()
    for i in range(n):
        ParentArray[i] = i+1
    return ParentArray, RateArray

def Union(i, j, ParentArray, RateArray):
    """
    Joins two nodes to the same tree (Using Union by Rank method)

    See Algorithms.py (Disjoint Set) for full documentation
    """
    Pi, Pj = ParentArray[i-1], ParentArray[j-1] # Parent of I & J
    Temp_I, Temp_J = i,j # Value of node I & J
    while Pi != Temp_I: # Loop till we find I's root
        Temp_I = Pi
        Pi = ParentArray[Temp_I-1]
    while Pj != Temp_J: # Loop till we find J's root
        Temp_J = Pj
        Pj = ParentArray[Temp_J-1]
    if Pi == Pj: # If root's are same, they belong to same tree. They're united already
        return 
    if RateArray[Pi-1] > RateArray[Pj-1]: # If I has higher height, add J tree to I tree by pointing J's root to I's root
        ParentArray[Pj-1] = Pi
    elif RateArray[Pi-1] < RateArray[Pj-1]: # If J has higher height, add I tree to J tree by pointing I's root to J's root
        ParentArray[Pi-1] = Pj
    else: # If heights are same, add J tree to I tree and increase I height++ (We can append in any direction)
        ParentArray[Pj-1] = Pi
        RateArray[Pi-1] += 1

def Find(i):
    """
    Joins node and subsequent neighbours in tree directly to the root (Using Path Compression method)    
    
    See Algorithms.py (Disjoint Set) for full documentation
    """
    parent = ParentArray[i-1]
    if ParentArray[parent-1] != parent:
        ParentArray[i-1] = Find(ParentArray[parent-1]) # Recursively calls the function till root is found
    return ParentArray[i-1]

def Connected(i,j):
    if 1<= i<= n*n and 1<= j<= n*n:
        print(f"{i} -> {j}: ",Find(i) == Find(j))

# Create maze and pick puzzle
maze = makeMaze(3)
ParentArray, RateArray = MakeSet(n*n)

# Solve maze
for i in range(1, n*n+1):
    row, col = IndexToGrid(i)
    neighbours = maze[row][col].neighbours()
    for neighbour in neighbours:
        if eval(neighbour): # if neighbour has border
            continue
        cell = neighbour.find('.') # neighbour = cell + . + border
        if (Find(i) == Find(eval(neighbour[:cell]).location)): # if Node root == neighbour root
            continue
        if neighbour.endswith('Left') and not(maze[row][col].borderRight): # Right Neighbour
            Union(i, i+1, ParentArray, RateArray) # Link Paths
        elif neighbour.endswith('Right') and not(maze[row][col].borderLeft): # Left Neighbour
            Union(i, i-1, ParentArray, RateArray) # Link Paths
        elif neighbour.endswith('Up') and not(maze[row][col].borderDown): # Down Neighbour
            Union(i, i+n, ParentArray, RateArray) # Link Paths
        elif neighbour.endswith('Down') and not(maze[row][col].borderUp): # Up Neighbour
            Union(i, i-n, ParentArray, RateArray) # Link Paths

# Check if two cells are connected (Puzzle 1 & 2) 3x3
Connected(1,3)
Connected(2,9)

# To prevent Error for Code Block below
if n < 8:
    import sys
    sys.exit()
    
# 3 starting points. Which is connected to the Destination? (Puzzle 3) 8x8    
Point_A, Point_B, Point_C, destination = 1, 32, 33, 30
pointName = ["Point A", "Point B", "Point C"]   
for index, i in enumerate([Point_A, Point_B, Point_C]):
    if Find(i) == Find(destination):
        name = pointName[index]
        print(f"{name} is connected to the goal")
